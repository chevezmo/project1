from repository.database import check_user_info, get_user_info, get_requests, get_history, get_stats

def test_check_user_info():
    assert check_user_info(dict(username = "sprettyjohns", password = "iVToNy")) == True

def test_check_user_info_incorrect_password():
    assert check_user_info(dict(username = "sprettyjohns", password = "ivory")) == False

def test_check_user_info_username_not_in_database():
    assert check_user_info(dict(username = "mchevez", password = "password")) == False

def test_get_user_info():
    assert get_user_info("rbritt") == (2, "Randie", "Britt", False)

def test_get_user_info_user_not_found():
    assert get_user_info("mchevez") == None

def test_get_requests():
    assert get_requests(3) == [("Randie", "Britt", "Excel Training", "$199.88", "Education or Training", "Pending", 3)]

def test_get_requests_no_requests():
    assert get_requests(2) == None

def test_get_history():
    assert get_history(5) == [(4, 5, "Plane Ticket - Toronto to New York - Round Trip", "$547.36", "Travel", "Cancelled")]

def test_get_history_multiple():
    assert get_history(2) == [(2, 2, "Office Supplies", "$21.25", "Supplies or Tools", "Rejected"), (3, 2, "Excel Training", "$199.88", "Education or Training", "Pending")]

def test_get_history_no_requests():
    assert get_history(3) == None

def test_get_history_user_not_found():
    assert get_history(10) == None

def test_get_stats():
    assert get_stats(1) == [(1, 0, 1, 0, 0)]

def test_get_stats_multiple():
    assert get_stats(2) == [(2, 1, 0, 1, 0)]

def test_get_stats_no_requests():
    assert get_stats(4) == [(0, None, None, None, None)]

def test_get_stats_user_not_found():
    assert get_stats(10) == [(0, None, None, None, None)]