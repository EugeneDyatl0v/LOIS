class PrettyWriter:
    @staticmethod
    def print(answers):
        ans = ''
        for map in answers:
            for key in map.keys():
                if map[key][0] == map[key][1]:
                    ans = ans + 'X' + str(key) + '=' + str(map[key][0]) +' '
                else:
                    ans = ans + 'X' + str(key) + '=' + str(map[key]) + ' '
            ans = ans + '\n'
        print(ans)