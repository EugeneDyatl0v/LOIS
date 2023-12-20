import re


class ParseFile:
    __SETS_PATTERN = r'^[A-Z]+=\{(?:<[A-Z],\d+(?:\.\d+)?>,)+<[A-Z],\d+(?:\.\d+)?>\}$'
    __IMPLICATIONS_PATTERN = r'^[A-Z]->[A-Z]$'
    __CASH = {
        "facts": {},
        "rules": []
    }

    @staticmethod
    def parse_file(url: str):
        txt = ParseFile.__open_file(url).replace(' ', '')
        sets = re.findall(ParseFile.__SETS_PATTERN, txt, re.MULTILINE)

        for current_set in sets:
            find_set_name = r'[A-Z]+'
            set_name = re.findall(find_set_name, current_set)
            ParseFile.__CASH["facts"][set_name[0]] = str

            find_dataset = r'\{(?:<[A-Z],\d+(?:\.\d+)?>,)+<[A-Z],\d+(?:\.\d+)?>\}'
            dataset = re.findall(find_dataset, current_set)[0]

            ParseFile.__CASH["facts"][set_name[0]] = dataset

        implications = re.findall(ParseFile.__IMPLICATIONS_PATTERN, txt, re.MULTILINE)
        for implication in implications:
            values = implication.split('->')
            ParseFile.__CASH["rules"].append((values[0], values[1]))

        return ParseFile.__CASH

    @staticmethod
    def __open_file(url: str) -> str:
        with open(url) as file:
            txt = file.read()
        return txt
