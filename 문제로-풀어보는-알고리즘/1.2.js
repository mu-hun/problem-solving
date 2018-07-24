function factorial2(n) {
    if (n == 1) return 1;
    else n * factorial2(n-1);
}

factorial2(3);