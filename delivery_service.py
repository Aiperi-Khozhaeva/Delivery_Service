import sys

# robots_weight = [1, 2, 2, 3], это список интов limit = 3, инт
# масса роботов, вернет количество платформ - 3 инт


def delivery_service(robots_weight: list[int], limit: int) -> int:
    robots_weight = sorted(robots_weight)
    count: int = 0
    # platform_ability == limit
    left = 0
    # max_value = robots_weight[left] + robots_weight[right]
    right = len(robots_weight) - 1
    while left <= right:
        if left == right:
            count += 1
            break
        elif robots_weight[left] + robots_weight[right] <= limit:
            count += 1
            left += 1
            right -= 1
        elif robots_weight[left] + robots_weight[right] > limit:
            count += 1
            right -= 1
            if robots_weight[right] <= limit:
                count += 1
                right -= 1
    return count


def main():
    robots_weight = sys.stdin.readline().strip()
    robots_weight = robots_weight.split(' ')
    robots_weight = [int(i) for i in robots_weight]
    limit = int(sys.stdin.readline().strip())
    result = delivery_service(robots_weight, limit)
    print(result)


if __name__ == '__main__':
    main()
