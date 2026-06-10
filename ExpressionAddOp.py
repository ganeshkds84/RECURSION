class Solution:
    def addOperators(self, s: str, target: int):
        # Your code goes here
        res = []

        def backtrack(index, path, curr_value, prev):
            
            if index == len(num):
                if curr_value == target:
                    res.append(path)
                return

            for i in range(index, len(num)):

                # Avoid numbers like 05, 00, 012
                if i > index and num[index] == '0':
                    break

                curr_str = num[index:i + 1]
                curr_num = int(curr_str)

                # First number
                if index == 0:
                    backtrack(
                        i + 1,
                        curr_str,
                        curr_num,
                        curr_num
                    )

                else:
                    # +
                    backtrack(
                        i + 1,
                        path + "+" + curr_str,
                        curr_value + curr_num,
                        curr_num
                    )

                    # -
                    backtrack(
                        i + 1,
                        path + "-" + curr_str,
                        curr_value - curr_num,
                        -curr_num
                    )

                    # *
                    backtrack(
                        i + 1,
                        path + "*" + curr_str,
                        curr_value - prev + prev * curr_num,
                        prev * curr_num
                    )
        backtrack(0,'',0,0)
        return res
    
if __name__=='__main__':
    num = "123"
    target = 6
    Ashu=Solution()
    print(Ashu.addOperators(num,target))