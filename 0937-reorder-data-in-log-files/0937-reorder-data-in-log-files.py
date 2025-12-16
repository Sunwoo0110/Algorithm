class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_list, let_list = [], []

        for log in logs:
            id_, content = log.split(" ", 1)
            if content[0].isdigit():
                dig_list.append(log)
            else:
                let_list.append((content, id_, log))

        let_list.sort()

        return [log for _, _, log in let_list]+dig_list





        