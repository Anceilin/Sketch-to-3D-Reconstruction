import numpy as np


def read_header(fp):
    line = fp.readline().strip()

    if not line.startswith(b'#binvox'):
        raise IOError('Not a binvox file')

    dims = list(map(int, fp.readline().strip().split(b' ')[1:]))
    translate = list(map(float, fp.readline().strip().split(b' ')[1:]))
    scale = float(fp.readline().strip().split(b' ')[1])

    fp.readline()

    return dims, translate, scale


def read(fp):
    dims, translate, scale = read_header(fp)

    raw = fp.read()

    size = dims[0] * dims[1] * dims[2]

    data = np.zeros(size, dtype=bool)

    index = 0
    i = 0

    while i < len(raw):
        value = raw[i]
        count = raw[i + 1]

        i += 2

        if value:
            data[index:index + count] = True

        index += count

    data = data.reshape(dims)

    class VoxelModel:
        pass

    model = VoxelModel()

    model.data = data
    model.dims = dims
    model.translate = translate
    model.scale = scale

    return model