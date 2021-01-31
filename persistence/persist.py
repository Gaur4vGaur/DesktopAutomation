import pickle


PERSISTENCE_PATH = '../publication.data'


def read(file_path):
    file_data = open(file_path, 'rb')
    data = pickle.load(file_data)
    file_data.close()
    return data


def update(data, file_path):
    file_write_data = open(file_path, 'wb')
    pickle.dump(data, file_write_data)
    file_write_data.close()


if __name__ == "__main__":
    dataset = {'Bart':75, 'Lisa':98, 'Milhouse':80, 'Nelson':65}
    update(PERSISTENCE_PATH, dataset)
    print(read(PERSISTENCE_PATH).get("Bart"))


