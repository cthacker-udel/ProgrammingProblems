using ull = unsigned long long;

ull exp_sum(unsigned int n)
{
    if (n == 0)
    {
        return 0;
    }
    unsigned long long result = 1;
    for (int i = 1; i < n; i++)
    {
        result *= 1 / 1 - pow(n, i);
    }
    return result;
}

int main(void)
{
    exp_sum(5);
}