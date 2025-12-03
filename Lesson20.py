class Blobservation:
    def __init__(self, h, w=None):
        if w is None:
            w = h
        if not (8 <= h <= 50 and 8 <= w <= 50):
            raise ValueError("Room dimensions must be between 8 and 50.")
        self.h, self.w = h, w
        self.blobs = []

    def populate(self, blob_list):
        if not isinstance(blob_list, list):
            raise ValueError("Invalid blob data.")
        merged = {}
        for b in blob_list:
            if not isinstance(b, dict) or not all(k in b for k in ('x', 'y', 'size')):
                raise ValueError("Invalid blob data.")
            x, y, s = b['x'], b['y'], b['size']
            if not (0 <= x < self.h and 0 <= y < self.w and 1 <= s <= 20):
                raise ValueError("Invalid blob data.")
            key = (x, y)
            merged[key] = {
                'x': x,
                'y': y,
                'size': merged.get(key, {'size': 0})['size'] + s
            }
        self.blobs = list(merged.values())

    def move(self, iterations=1):
        if not isinstance(iterations, int) or iterations < 0:
            raise ValueError("Number of iterations must be a positive integer.")
        for _ in range(iterations):
            self._move_once()

    def print_state(self):
        return sorted([[b['x'], b['y'], b['size']] for b in self.blobs], key=lambda v: (v[0], v[1]))

    def _move_once(self):
        new_positions = {}
        for blob in sorted(self.blobs, key=lambda b: (b['x'], b['y'])):
            if blob['size'] == 1:
                nx, ny = blob['x'], blob['y']
            else:
                target = self._find_target(blob)
                if not target:
                    nx, ny = blob['x'], blob['y']
                else:
                    dx = (target['x'] > blob['x']) - (target['x'] < blob['x'])
                    dy = (target['y'] > blob['y']) - (target['y'] < blob['y'])
                    nx = max(0, min(self.h - 1, blob['x'] + dx))
                    ny = max(0, min(self.w - 1, blob['y'] + dy))

            key = (nx, ny)
            if key in new_positions:
                new_positions[key]['size'] += blob['size']
            else:
                new_positions[key] = {'x': nx, 'y': ny, 'size': blob['size']}

        self.blobs = list(new_positions.values())

    def _find_target(self, blob):
        smaller = [b for b in self.blobs if b['size'] < blob['size']]
        if not smaller:
            return None

        def priority(b):
            dist = max(abs(blob['x'] - b['x']), abs(blob['y'] - b['y']))
            return (dist, -b['size'], b['x'], b['y'])
       

