
import json
import gzip


def save_gzipped_json(data, json_path):
    with gzip.GzipFile(json_path, 'w') as fout:
        fout.write(json.dumps(data).encode('utf-8'))


def load_gzipped_json(json_path):
    with gzip.open(json_path, 'rb') as f:
        ret = json.loads(f.read().decode('ascii'))
    return ret
