function GetFiveSum(n)
    local sum = 0
    for i=11, tonumber(n) do
        local rotation = GetRotation(i)
        if IsDivisible(i, rotation) then
            sum = sum + i
        end
    end
    return string.sub(tostring(sum), -5)
end

function GetRotation(n)
    local r = n % 10
    local m = math.floor(n / 10)
    return math.floor(m + (r * (10 ^ m)))
end

function IsDivisible(n, rotation)
    return rotation % n == 0
end

print(GetFiveSum(arg[1]))