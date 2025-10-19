import pytest
from utils.excel_updater import update_excel_status


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    A special pytest hook that runs for each test. We use it to capture
    the test report (its result) and attach it to the test item itself.
    This makes the test's outcome accessible to our fixtures later on.
    """
    # This executes the test and gets the result object
    outcome = yield
    report = outcome.get_result()

    # We store the report object on the test item. The 'rep_...' attributes
    # are dynamically created (e.g., rep_setup, rep_call, rep_teardown).
    setattr(item, "rep_" + report.when, report)


@pytest.fixture(autouse=True)
def excel_logger(request):
    """
    This is an 'autouse' fixture, meaning pytest will automatically run it
    for every single test. Its job is to check for our custom '@pytest.mark.tc'
    marker and, after the test is done, call the Excel update function.
    """
    # This part of the code runs *before* your test function
    marker = request.node.get_closest_marker("tc")

    # 'yield' passes control to your actual test function
    yield

    # This part of the code runs *after* your test is complete (teardown)
    if not marker:
        return  # Do nothing if the test doesn't have our custom 'tc' marker

    test_case_id = marker.kwargs.get("id")
    sheet_name = marker.kwargs.get("sheet")

    if not test_case_id or not sheet_name:
        return  # Skip if the marker is missing id or sheet name

    # Get the test outcome from the report object we attached in the hook
    report = getattr(request.node, "rep_call", None)
    status = "skipped"
    error = None
    duration = 0.0

    if report:
        duration = report.duration
        if report.passed:
            status = "passed"
        elif report.failed:
            status = "failed"
            error = str(report.longrepr)  # Get the full error message

    # Also check if the test was skipped during its setup phase
    setup_report = getattr(request.node, "rep_setup", None)
    if setup_report and setup_report.skipped:
        status = "skipped"
        if setup_report.longrepr:
            # Extract the skip reason
            error = setup_report.longrepr[2]

            # Call the function that writes the result to the Excel file
    update_excel_status(
        test_case_id=test_case_id,
        sheet_name=sheet_name,
        status=status,
        duration=duration,
        error_message=error
    )

