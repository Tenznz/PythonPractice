class Color:
    def __init__(self):
        self.x = "red"
        self.y = "blue"
        self.z = "green"


def get_dict(color_obj):
    dict_data={
        "x": color_obj.x,
        "y": color_obj.y,
        "z": color_obj.z
    }
    return dict_data


if __name__ == "__main__":
    color_obj = Color()
    print(get_dict(color_obj))
    print(color_obj.__dict__)
