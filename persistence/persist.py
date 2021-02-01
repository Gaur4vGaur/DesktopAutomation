import pickle

PERSISTENCE_PATH = './publication.data'

PUB_READ_COUNT = 'pub_read_count'
LAST_COUNT = 'last_count'


def read(file_path):
    # print("---------------")
    # print(file_path)
    # print(os.path.abspath(file_path))
    # print(os.path.isfile(file_path))
    # print("---------------")
    file_data = open(file_path, 'rb')
    data = pickle.load(file_data)
    file_data.close()
    return data


def update(file_path, data):
    file_write_data = open(file_path, 'wb')
    pickle.dump(data, file_write_data)
    file_write_data.close()


def test_pub_details():
    update(PERSISTENCE_PATH, {LAST_COUNT: 97, PUB_READ_COUNT: 0})


if __name__ == "__main__":
    test_pub_details()
    r = read(PERSISTENCE_PATH).get(PUB_READ_COUNT)
    print(type(r))


