class Solution:
    def average(self, salary):
        smallest = float('inf')
        largest = float('-inf')
        sum = 0
        for i in range(len(salary)):
            if salary[i] > largest:
                largest = salary[i]
            if salary[i] < smallest:
                smallest = salary[i]
            sum += salary[i]

        final_sum = sum - (smallest + largest)
        result = final_sum / (len(salary)-2)
        print(result)

    def average2(self, salary):
        salary.remove(max(salary))
        salary.remove(min(salary))
        print(sum(salary) / len(salary))


salary = [4000,3000,1000,2000]
x = Solution()
x.average(salary)
x.average2(salary)