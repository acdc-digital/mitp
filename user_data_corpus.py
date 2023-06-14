import os
import json

class UserDataCorpus:
    def __init__(self, data_directory="user_data"):
        self.data_directory = data_directory
        if not os.path.exists(self.data_directory):
            print(f"Directory '{self.data_directory}' does not exist. Please create the directory and add user data files.")
            self.user_data = {}
        else:
            self.user_data = self.load_user_data()

    def load_user_data(self):
        user_data = {}
        for filename in os.listdir(self.data_directory):
            if filename.endswith(".json"):
                user_id = os.path.splitext(filename)[0]
                with open(os.path.join(self.data_directory, filename), "r") as file:
                    user_data[user_id] = json.load(file)
        return user_data

    def get_user_data(self, user_id):
        return self.user_data.get(user_id, None)

    def update_user_data(self, user_id, new_data):
        if not os.path.exists(self.data_directory):
            print(f"Directory '{self.data_directory}' does not exist. Please create the directory before updating user data.")
        else:
            self.user_data[user_id] = new_data
            with open(os.path.join(self.data_directory, f"{user_id}.json"), "w") as file:
                json.dump(new_data, file)
