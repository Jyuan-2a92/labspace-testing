import os
from unittest.mock import patch, mock_open
from .quiz import Question, run_quiz, create_quiz, save_quiz, load_quiz

def test_question_to_dict():
    question = Question("What is the capital of France?", "Paris")
    assert question.to_dict() == {"prompt": "What is the capital of France?", "answer": "Paris"}

def test_question_from_dict():
    data = {"prompt": "What is the capital of France?", "answer": "Paris"}
    question = Question.from_dict(data)
    assert question.prompt == "What is the capital of France?"
    assert question.answer == "Paris"

@patch('quiz.input')
def test_run_quiz(mock_input):
    mock_input.side_effect = ["Paris", "", "done"]
    questions = [Question("What is the capital of France?", "Paris")]
    with patch('quiz.print') as mock_print:
        run_quiz(questions)
        mock_print.assert_has_calls([
            mock.call("What is the capital of France?"),
            mock.call("Your answer: Your final score is 1/1")
        ])

@patch('builtins.open', new_callable=mock_open, read_data='[{"prompt": "What is the capital of France?", "answer": "Paris"}]')
def test_load_quiz(mock_file):
    questions = load_quiz("test_quiz")
    assert len(questions) == 1
    question = questions[0]
    assert question.prompt == "What is the capital of France?"
    assert question.answer == "Paris"

@patch('builtins.open', new_callable=mock_open)
def test_save_quiz(mock_file):
    questions = [Question("What is the capital of France?", "Paris")]
    save_quiz("test_quiz", questions)
    mock_file.assert_called_once_with('test_quiz.json', 'w')
    mock_file().write.assert_called_once()

@patch('quiz.input')
def test_create_quiz(mock_input):
    mock_input.side_effect = ["Capital of France?", "Paris", "Test Quiz"]
    with patch('builtins.open') as mock_open:
        create_quiz()
        mock_open.assert_called_once_with('Test Quiz.json', 'w')
        assert mock_open().write.call_args_list == [mock.call('[{"prompt": "Capital of France?", "answer": "Paris"}]')]

if __name__ == "__main__":
    pytest.main(["--cov-branch", "-v"])
