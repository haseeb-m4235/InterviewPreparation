from typing_extensions import TypedDict
from dataclasses import dataclass

class InterviewerState(TypedDict):
    job_description: str
    questions_list: list[str]
    current_question: str
    current_index: int
    answers_list: list[str]
    evaluation_report: str 

@dataclass
class Context:
    model_name: str