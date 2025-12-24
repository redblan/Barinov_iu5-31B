import pytest
from refactored_rk1_varA2 import DataService, StudentClassService

class TestStudentClassService:
    @pytest.fixture
    def service(self):
        return StudentClassService(DataService())

    def test_task_a1(self, service):
        result = service.task_a1()
        assert len(result) == 5
        class_names = [class_name for _, _, class_name in result]
        assert class_names == sorted(class_names)
        assert result[0][2] == 'математический класс'
        assert result[0][0] == 'Иванов'
        assert result[0][1] == 85
        math_class_items = [item for item in result if item[2] == 'математический класс']
        math_students = [student for student, _, _ in math_class_items]
        assert math_students == ['Иванов', 'Козлов']

    def test_task_a2(self, service):
        result = service.task_a2()
        assert len(result) == 3
        total_scores = [score for _, score in result]
        assert total_scores == sorted(total_scores, reverse=True)
        result_dict = dict(result)
        assert result_dict['математический класс'] == 180
        assert result_dict['физический класс'] == 180
        assert result_dict['химический класс'] == 78

    def test_task_a3(self, service):
        result = service.task_a3()
        assert isinstance(result, dict)
        assert len(result) == 3
        assert 'математический класс' in result
        assert 'физический класс' in result
        assert 'химический класс' in result
        assert result['математический класс'] == ['Иванов', 'Козлов']
        assert result['физический класс'] == ['Петров', 'Смирнов']
        assert result['химический класс'] == ['Сидоров']

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
