from .exceptions import ItemNotFoundError


class FakeDB:
    # Simulates a database of random items.
    db = {
        'items': [
            {
                'name': 'Potato',
                'description': 'A nice potato.',
                'price': 2.50,
            },
            {
                'name': 'Tomato',
                'description': 'A nice tomato.',
                'price': 2.80,
            },
        ]
    }

    def normalize_item_id(self, item_id: int):
        """Normalize the item_id to 0-based."""
        return item_id - 1

    def get_item_or_error(self, item_id: int):
        item_id = self.normalize_item_id(item_id)
        try:
            return self.db['items'][item_id]
        except IndexError:
            raise ItemNotFoundError(f'Item with ID {item_id + 1} was not found.')

    def get_items(self):
        return self.db['items']

    def get_item(self, item_id: int):
        item = self.get_item_or_error(item_id)
        return item

    def add_item(self, item: dict):
        self.db['items'].append(item)
        return item

    def update_item(self, item_id: int, fields_to_update: dict):
        item = self.get_item_or_error(item_id)
        item.update(fields_to_update)

        item_id = self.normalize_item_id(item_id)
        self.db['items'].pop(item_id)
        self.db['items'].insert(item_id, item)

        return fields_to_update

    def delete_item(self, item_id: int):
        self.get_item_or_error(item_id)

        item_id = self.normalize_item_id(item_id)
        self.db['items'].pop(item_id)
