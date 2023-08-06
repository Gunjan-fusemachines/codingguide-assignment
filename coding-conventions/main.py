import json

class StudentManager:
    """
    Class to manage student records.

    Attributes:
        records (list): List to store student records.

    Methods:
        add_student(student_id, name, age, grade): Add a new student record.
        search_student(identifier): Search for a student by student_id or name.
        update_student(identifier, field, new_value): Update student information.
    """
    def __init__(self, filename):
        """
        Initialize the StudentManager.

        Args:
            filename (str): The name of the JSON file to save records to.
        """
        self.records = []
        self.filename = filename

    def _save_records_to_file(self):
        """
        Save records to JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.records, file)

    def _load_records_from_file(self):
        """
        Load records from JSON file.
        """
        try:
            with open(self.filename, 'r') as file:
                self.records = json.load(file)
        except FileNotFoundError:
            self.records = []

    def add_student(self, student_id, name, age, grade):
        """
        Add a new student record.

        Args:
            student_id (int): Student's ID.
            name (str): Student's name.
            age (int): Student's age.
            grade (str): Student's grade.
        """
        student = {
            'student_id': student_id,
            'name': name,
            'age': age,
            'grade': grade
        }
        self.records.append(student)
        self._save_records_to_file()

    def search_student(self, identifier):
        """
        Search for a student by student_id or name.

        Args:
            identifier (int or str): Student's ID or name.

        Returns:
            dict or None: Student's information (age and grade) or None if not found.
        """
        self._load_records_from_file()
        for student in self.records:
            if student['student_id'] == identifier or student['name'] == identifier:
                return {'age': student['age'], 'grade': student['grade']}
        return None

    def update_student(self, identifier, field, new_value):
        """
        Update student information by student_id or name (age or grade).

        Args:
            identifier (int or str): Student's ID or name.
            field (str): Field to update ('age' or 'grade').
            new_value (int or str): New value for the field.
        """
        self._load_records_from_file()
        for student in self.records:
            if student['student_id'] == identifier or student['name'] == identifier:
                student[field] = new_value
                self._save_records_to_file()
                return

def main():
    """
    Main function to demonstrate student record management.
    """
    manager = StudentManager('coding-conventions/student_records.json')

    manager.add_student(1, 'Alice', 18, 'A')
    manager.add_student(2, 'Bob', 17, 'B')
    manager.add_student(3, 'Charlie', 19, 'C')

    print(manager.search_student(1))
    print(manager.search_student('Bob'))

    manager.update_student(2, 'age', 18)
    manager.update_student('Charlie', 'grade', 'B')

    print(manager.search_student(2))
    print(manager.search_student('Charlie'))

if __name__ == "__main__":
    main()
