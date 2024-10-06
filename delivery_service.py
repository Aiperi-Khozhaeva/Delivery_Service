import sys

# id успешной посылки - 119794161


def delivery_service(robots_weight: list[int], limit: int) -> int:
    robots_weight = sorted(robots_weight)
    count: int = 0
    x, y = 0, len(robots_weight) - 1
    while x <= y:
        if robots_weight[x] + robots_weight[y] <= limit:
            x += 1
        y -= 1
        count += 1
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
