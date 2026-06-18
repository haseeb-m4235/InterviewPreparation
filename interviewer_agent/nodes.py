from interviewer_agent.models import InterviewerState

def human_node(state: InterviewerState) -> str:
    if not state['job_description']:
        # Interrupt and ask for job description
        # update job descritpion in state
        # next node is Questions_creator
        pass
    else:
        # Interrupt with the current question, append answer to answers_list, and next node is asker
        pass

def question_creator(state: InterviewerState) -> str:
    # Get the job description
    # Prepare prompt for question creation
    # Call LLM to generate questions based on the job description
    # Extract questions
    # Update questions_list in state
    # Next node is asker
    pass

def job_description_check(state: InterviewerState) -> str:
    if not state['questions_list']:
        return 'QuestionCreator'
    else:
        return 'Asker'

def asker(state: InterviewerState) -> str:
    # update the state's current question, increment current_index in state
    # next node is questions_ender
    pass

def questions_ender(state: InterviewerState) -> str:
    # Check if current_index in state is less than length of questions list
    # Yes: next node is human_node
    # No: next node is evaluator
    pass

def evaluator(state: InterviewerState) -> str:
    # Get Questions list and answers list from state
    # Prepare prompt for evaluation
    # call llm to generate report
    # Extract report
    # Update evaluation_report in state
    pass