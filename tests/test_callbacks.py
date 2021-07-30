import unittest
from unittest.mock import Mock

import nio

from my_project_name.callbacks import Callbacks
from my_project_name.storage import Storage

from tests.utils import make_awaitable, run_coroutine


class CallbacksTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # Create a Callbacks object and give it some Mock'd objects to use
        self.fake_client = Mock(spec=nio.AsyncClient)
        self.fake_client.user = "@fake_user:example.com"

        self.fake_storage = Mock(spec=Storage)

        # We don't spec config, as it doesn't currently have well defined attributes
        self.fake_config = Mock()

        self.callbacks = Callbacks(
            self.fake_client, self.fake_storage, self.fake_config
        )

if __name__ == "__main__":
    unittest.main()
