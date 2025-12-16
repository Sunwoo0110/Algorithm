class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_list, let_list = [], []

        for log in logs:
            log_list = log.split(" ")
            word = log_list[1]

            if word.isdigit():
                dig_list.append(log)
            else:
                let_list.append(log)
        
        let_list.sort(key = lambda x: (x.split(" ")[1:], x.split(" ")[0]))
        return let_list+dig_list





        