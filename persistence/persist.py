import pickle


PERSISTENCE_PATH = '../publication.data'

PUB_READ_COUNT = 'pub_read_count'
LAST_COUNT = 'last_count'
PUBLICATION_PATH = "publication_update.data"


def read(file_path):
    file_data = open(file_path, 'rb')
    data = pickle.load(file_data)
    file_data.close()
    return data


def update(file_path, data):
    file_write_data = open(file_path, 'wb')
    pickle.dump(data, file_write_data)
    file_write_data.close()


def test_pub_details():
    update(PUBLICATION_PATH, {LAST_COUNT: 97, PUB_READ_COUNT: 0})

# if __name__ == "__main__":
#     dataset = {'Bart':75, 'Lisa':98, 'Milhouse':80, 'Nelson':65}
#     update(dataset, PERSISTENCE_PATH)
#     print(read(PERSISTENCE_PATH).get("Bart"))


