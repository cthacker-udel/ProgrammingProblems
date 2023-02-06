from typing import List, Optional, Set


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        permutations = (
            set()
        )  # where we store the permutations which is [index started at, permutation] in STR (json stringify basically)
        self.generate_perms(s, permutations)  # populates permutation array
        total_count = 0  # count of total unique characters
        print(permutations)  # prints the permutations
        for each_perm in permutations:  # for each permutation in permutations
            each_perm = each_perm.strip("][").split(", ")  # converts it back to a list
            total_count += sum(
                [1 if each_perm[1].count(x) == 1 else 0 for x in set(each_perm[1])]
            )  # sums up the unique characters, UNIQUE MEANING IT ONLY APPEARS ONCE, AAB = 1 BECAUSE B OCCURS 1 WHILE A OCCURS 2
        return total_count

    def generate_perms(
        self, s: str, permutations: List[str], current_sub: Optional[str] = "", offset=0
    ) -> None:

        for i in range(len(s)):
            current_sub += s[i]  # Choice
            if (
                str([offset, current_sub]) not in permutations
            ):  # Validation + recursive call if valid choice
                permutations.add(
                    str([offset, current_sub])
                )  # add current permutation to stack
                self.generate_perms(
                    s[i + 1 :], permutations, current_sub, offset
                )  # generate next permutation
            current_sub = current_sub[1:]  # move to next character in perm
            offset += 1  # increment offset due to index increasing in loop iteration


if __name__ == "__main__":
    s = "DELQGVWNZKIJJPSXOVWWIZUXCEGWSQLESNSRBMKZARFPAXSVWQEZDENDAHNNIBHGHTFDLPGDLFXMIYRFNLMXHNPIFUAXINXPXLCTTJNLGGMKJIOEWBECNOFQPVCIKIAZMNGHEHFMCPWSMJTMGVSXTOGCGUYKFMNCGLCBRAFJLJVPIVDOLJBURULPGXBVDCEWXXXLTRMSHPKSPFDGNVOCZWDXJUWVNAREDOKTZMIUDKDQWWWSAEUUDBHMWZELOSBIHMAYJEMGZPMDOOGSCKLVHTGMETHUISCLJKDOQEWGVBULEMUXGTRKGXYFDIZTZWMLOFTCANBGUARNWQEQWGMIKMORVQUZANJNRNPMJWYLVHWKDFLDDBBMILAKGFROEQAMEVONUVHOHGPKLBPNYZFPLXNBCIFENCGIMIDCXIIQJWPVVCOCJTSKSHVMQJNLHSQTEZQTTMOXUSKBMUJEJDBJQNXECJGSZUDENJCPTTSREKHPRIISXMWBUGMTOVOTRKQCFSDOTEFPSVQINYLHXYVZTVAMWGPNKIDLOPGAMWSKDXEPLPPTKUHEKBQAWEBMORRZHBLOGIYLTPMUVBPGOOOIEBJEGTKQKOUURHSEJCMWMGHXYIAOGKJXFAMRLGTPNSLERNOHSDFSSFASUJTFHBDMGBQOKZRBRAZEQQVWFRNUNHBGKRFNBETEDJIWCTUBJDPFRRVNZENGRANELPHSDJLKVHWXAXUTMPWHUQPLTLYQAATEFXHZARFAUDLIUDEHEGGNIYICVARQNRJJKQSLXKZZTFPVJMOXADCIGKUXCVMLPFJGVXMMBEKQXFNXNUWOHCSZSEZWZHDCXPGLROYPMUOBDFLQMTTERGSSGVGOURDWDSEXONCKWHDUOVDHDESNINELLCTURJHGCJWVIPNSISHRWTFSFNRAHJAJNNXKKEMESDWGIYIQQRLUUADAXOUEYURQRVZBCSHXXFLYWFHDZKPHAGYOCTYGZNPALAUZSTOU"
    sol = Solution()
    print(sol.uniqueLetterString(s))
