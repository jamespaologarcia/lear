# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Test Suites to ensure that the worker is operating correctly."""
import pytest

from entity_emailer.worker import process_email


def test_process_filing_missing_app(app, session):
    """Assert that a filling will fail with no flask app supplied."""
    # setup
    email_msg = {'email': {'type': 'bn'}}

    # TEST
    with pytest.raises(Exception):
        process_email(email_msg, flask_app=None)


def test_process_bn_email(app, session):
    """Assert that a BN email msg is processed correctly."""
    # setup
    email_msg = {'email': {'type': 'bn'}}

    # TEST
    process_email(email_msg, app)

    # Get modified data to be implemented after email is sending

    # verify what was sent to be implemented


def test_process_incorp_email(app, session):
    """Assert that an INCORP email msg is processed correctly."""
    # setup
    email_msg = {'email': {'type': 'incorp'}}

    # TEST
    process_email(email_msg, app)

    # Get modified data to be implemented after email is sending

    # verify what was sent to be implemented