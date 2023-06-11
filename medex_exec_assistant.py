from flask_socketio import SocketIO, emit
from medex_project.utils.interpretation import interpret_medical_data
from medex_project.utils.privacy_filter import apply_privacy_filter

socketio = SocketIO()

@socketio.on('message')
def handle_message(data):
    user_input = data['message']
    filtered_input = apply_privacy_filter(user_input)
    medex_assistant_response = interpret_medical_data(filtered_input)
    emit('medex_assistant_response', {'message': medex_assistant_response})