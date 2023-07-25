def create_data_folders() -> None:
    with open('data/user_data.json', 'w') as f:
        f.truncate()
    with open('data/system_info.json', 'w') as f:
        f.truncate()