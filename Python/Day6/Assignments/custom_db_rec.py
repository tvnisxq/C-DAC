class RecordNotFoundError(Exception):
    """Custom exception raised when a record with a specific name is not found."""
    pass


class DatabaseRecord:
    """Represents a single database record with a unique ID and data dictionary."""
    def __init__(self, record_id: int, data: dict):
        self.record_id = record_id
        self.data = data

    def __str__(self) -> str:
        return f"Record(id={self.record_id}, data={self.data})"

    def __repr__(self) -> str:
        return f"Record(id={self.record_id}, data={self.data})"


class ResultSetIterator:
    """Custom iterator to traverse through a collection of DatabaseRecord objects."""
    def __init__(self, records_list: list):
        self._records_list = records_list
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> DatabaseRecord:
        # Check if there are remaining records to iterate over
        if self._index < len(self._records_list):
            record = self._records_list[self._index]
            self._index += 1
            return record
        raise StopIteration


class DatabaseResultSet:
    """Represents a query result set supporting length, iteration, and dual indexing (integer index or name string lookup)."""
    def __init__(self, records_list: list):
        self._records_list = records_list

    def __len__(self) -> int:
        return len(self._records_list)

    def __iter__(self) -> ResultSetIterator:
        return ResultSetIterator(self._records_list)

    def __getitem__(self, key):
        if isinstance(key, int):
            # Handle integer-based indexing (raises IndexError automatically if out of bounds)
            return self._records_list[key]
        elif isinstance(key, str):
            # Handle string-based lookup searching by data["name"]
            for record in self._records_list:
                if record.data.get("name") == key:
                    return record
            # Raise custom exception if name is not found in any record
            raise RecordNotFoundError(f"Record with name '{key}' not found in database.")
        else:
            raise TypeError("Key must be an integer index or a string name.")


# Setup records
r1 = DatabaseRecord(101, {"name": "Alice", "role": "Admin"})
r2 = DatabaseRecord(102, {"name": "Bob", "role": "User"})

results = DatabaseResultSet([r1, r2])

# 1. Length
print(len(results))  # Output: 2

print("="*80)

# 2. Integer Indexing
print(results[0].data["role"])  # Output: Admin
print("="*80)

# 3. String lookup
record = results["Bob"]
print(record.record_id)  # Output: 102
print("="*80)

# 4. Iteration
for rec in results:
    print(rec.record_id)
print("="*80)
# Output:
# 101
# 102

# 5. Missing key lookup
try:
    missing = results["Charlie"]
except RecordNotFoundError as e:
    print(e)  # Output: Record with name 'Charlie' not found in database.