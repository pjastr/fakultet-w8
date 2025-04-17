import pytest

# Database connection counter
connection_count = 0


@pytest.fixture(scope="function")
def function_data():
    print("\n[Function] Creating new test data")
    return {"id": 1, "fresh": True}


@pytest.fixture(scope="module")
def db_connection():
    # Simulate expensive database connection
    global connection_count
    connection_count += 1
    print(f"\n[Module] Opening database connection #{connection_count}")

    # Setup - return connection
    connection = {"connected": True, "id": connection_count}
    yield connection

    # Teardown - close connection
    print(f"[Module] Closing database connection #{connection_count}")


# First test file (save as test_db_first.py)
def test_user_insertion(function_data, db_connection):
    print(f"  Running test_user_insertion with connection #{db_connection['id']}")
    assert db_connection["connected"] is True
    assert function_data["fresh"] is True


def test_user_query(function_data, db_connection):
    print(f"  Running test_user_query with connection #{db_connection['id']}")
    assert db_connection["connected"] is True
    assert function_data["fresh"] is True  # Always fresh because of function scope