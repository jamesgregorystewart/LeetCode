# O()
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full_bottles, empty_bottles, bottles_drunk = numBottles, 0, 0
        while full_bottles or empty_bottles >= numExchange:
            if empty_bottles >= numExchange:
                # if we can exchange we should
                full_bottles += 1
                empty_bottles -= numExchange
                numExchange += 1
                continue
            # can't exchange but we can drink!
            bottles_drunk += full_bottles
            empty_bottles += full_bottles
            full_bottles = 0
        return bottles_drunk
