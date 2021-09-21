import os
import sys
import time
import json
import unittest
from jc.exceptions import ParseError
import jc.parsers.ls_s

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# Set the timezone on POSIX systems. Need to manually set for Windows tests
if not sys.platform.startswith('win32'):
    os.environ['TZ'] = 'America/Los_Angeles'
    time.tzset()

# To create streaming output use:
# $ cat ls-al.out | jc --ls-s | jello -c > ls-al-streaming.json

class MyTests(unittest.TestCase):

    def setUp(self):
        # input
        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ls.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ls = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ls-al.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ls_al = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ls-al.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ls_al = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.11.6/ls-al.out'), 'r', encoding='utf-8') as f:
            self.osx_10_11_6_ls_al = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ls-al.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ls_al = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ls-alh.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ls_alh = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ls-alh.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ls_alh = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.11.6/ls-alh.out'), 'r', encoding='utf-8') as f:
            self.osx_10_11_6_ls_alh = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ls-alh.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ls_alh = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ls-alR.out'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ls_alR = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ls-alR.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ls_alR = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ls-alR.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ls_alR = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ls-lR-empty-folder.out'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ls_lR_empty_folder = f.read()

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ls-l-iso.out'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ls_l_iso = f.read()

        # output

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ls-al-streaming.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ls_al_streaming_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ls-al-streaming.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ls_al_streaming_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ls-al-streaming.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ls_al_streaming_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ls-alh-streaming.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ls_alh_streaming_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ls-alh-streaming.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ls_alh_streaming_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ls-alh-streaming.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ls_alh_streaming_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/centos-7.7/ls-alR-streaming.json'), 'r', encoding='utf-8') as f:
            self.centos_7_7_ls_alR_streaming_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ls-alR-streaming.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ls_alR_streaming_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ls-alR-streaming.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ls_alR_streaming_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/osx-10.14.6/ls-lR-empty-folder-streaming.json'), 'r', encoding='utf-8') as f:
            self.osx_10_14_6_ls_lR_empty_folder_streaming_json = json.loads(f.read())

        with open(os.path.join(THIS_DIR, os.pardir, 'tests/fixtures/ubuntu-18.04/ls-l-iso-streaming.json'), 'r', encoding='utf-8') as f:
            self.ubuntu_18_4_ls_l_iso_streaming_json = json.loads(f.read())

    def test_ls_empty_dir(self):
        """
        Test plain 'ls' on an empty directory
        """
        self.assertEqual(list(jc.parsers.ls_s.parse('', quiet=True)), [])

    def test_ls_centos_7_7(self):
        """
        Test plain 'ls /' on Centos 7.7 (raises ParseError)
        """
        g = jc.parsers.ls_s.parse(self.centos_7_7_ls.splitlines())
        with self.assertRaises(ParseError):
            list(g)

    def test_ls_al_centos_7_7(self):
        """
        Test 'ls -al /' on Centos 7.7
        """
        self.assertEqual(list(jc.parsers.ls_s.parse(self.centos_7_7_ls_al.splitlines())), self.centos_7_7_ls_al_streaming_json)

    def test_ls_al_ubuntu_18_4(self):
        """
        Test 'ls -al /' on Ubuntu 18.4
        """
        self.assertEqual(list(jc.parsers.ls_s.parse(self.ubuntu_18_4_ls_al.splitlines())), self.ubuntu_18_4_ls_al_streaming_json)

    def test_ls_al_osx_10_14_6(self):
        """
        Test 'ls -al /' on OSX 10.14.6
        """
        self.assertEqual(list(jc.parsers.ls_s.parse(self.osx_10_14_6_ls_al.splitlines())), self.osx_10_14_6_ls_al_streaming_json)

    def test_ls_alh_centos_7_7(self):
        """
        Test 'ls -alh /' on Centos 7.7
        """
        self.assertEqual(list(jc.parsers.ls_s.parse(self.centos_7_7_ls_alh.splitlines())), self.centos_7_7_ls_alh_streaming_json)

    def test_ls_alh_ubuntu_18_4(self):
        """
        Test 'ls -alh /' on Ubuntu 18.4
        """
        self.assertEqual(list(jc.parsers.ls_s.parse(self.ubuntu_18_4_ls_alh.splitlines())), self.ubuntu_18_4_ls_alh_streaming_json)

    def test_ls_alh_osx_10_14_6(self):
        """
        Test 'ls -alh /' on OSX 10.14.6
        """
        self.assertEqual(list(jc.parsers.ls_s.parse(self.osx_10_14_6_ls_alh.splitlines())), self.osx_10_14_6_ls_alh_streaming_json)

    def test_ls_alR_centos_7_7(self):
        """
        Test 'ls -alR /usr' on Centos 7.7
        """
        self.assertEqual(list(jc.parsers.ls_s.parse(self.centos_7_7_ls_alR.splitlines())), self.centos_7_7_ls_alR_streaming_json)

    def test_ls_alR_ubuntu_18_4(self):
        """
        Test 'ls -alR /usr' on Ubuntu 18.4
        """
        self.assertEqual(list(jc.parsers.ls_s.parse(self.ubuntu_18_4_ls_alR.splitlines())), self.ubuntu_18_4_ls_alR_streaming_json)

    def test_ls_alR_osx_10_14_6(self):
        """
        Test 'ls -alR /usr' on OSX 10.14.6
        """
        self.assertEqual(list(jc.parsers.ls_s.parse(self.osx_10_14_6_ls_alR.splitlines())), self.osx_10_14_6_ls_alR_streaming_json)

    def test_ls_lR_empty_folder_osx_10_14_6(self):
        """
        Test 'ls -lR' for empty directories on OSX 10.14.6
        """
        self.assertEqual(list(jc.parsers.ls_s.parse(self.osx_10_14_6_ls_lR_empty_folder.splitlines())), self.osx_10_14_6_ls_lR_empty_folder_streaming_json)

    def test_ls_l_iso_ubuntu_18_4(self):
        """
        Test 'ls -l --time-style=full-iso' for files with convertible dates on Ubuntu 18.4
        """
        self.assertEqual(list(jc.parsers.ls_s.parse(self.ubuntu_18_4_ls_l_iso.splitlines())), self.ubuntu_18_4_ls_l_iso_streaming_json)


if __name__ == '__main__':
    unittest.main()
