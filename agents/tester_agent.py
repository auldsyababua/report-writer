def handle_test(task: str) -> str:
    return """\
# Tests based only on the spec

def test_fetch_metrics_structure():
    metrics = fetch_metrics()
    assert isinstance(metrics, dict), "Metrics should be a dictionary"
    assert "revenue" in metrics
    assert "hashrate" in metrics
    assert "uptime" in metrics

def test_render_report_substitution():
    metrics = {
        "revenue": "$1000",
        "hashrate": "123 TH/s",
        "uptime": "99.9%",
        "carbon_offset": "5.5 tons"
    }
    with open("templates/test_template.txt", "w") as f:
        f.write("Revenue: {revenue}, Uptime: {uptime}")
    result = render_report("test", metrics)
    assert "Revenue: $1000" in result
    assert "Uptime: 99.9%" in result

# This test assumes API call will fail with bad token
def test_send_report_failure():
    code = send_report("123456", "test", "invalid_token")
    assert code != 200, "Expected failure status from invalid token"
"""
