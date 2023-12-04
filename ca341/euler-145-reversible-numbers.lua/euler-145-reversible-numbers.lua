function ReversibleNumbers(n)
    local total = 0
    for i=1, n-1 do
        if AllOdd(i + Reverse(i)) then
            total = total + 1
        end
    end
    return total
end

function Reverse(n)
    local s = tostring(n)
    local reversed = string.reverse(s)
    return tonumber(reversed)
end

function AllOdd(n)
    while n > 0 do
        local x = n % 10
        if x % 2 == 0 then
            return false
        end
        n = math.floor(n / 10)
    end
    return true
end

print(ReversibleNumbers(tonumber(arg[1])))