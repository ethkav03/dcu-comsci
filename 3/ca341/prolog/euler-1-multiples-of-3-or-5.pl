% Define the number of dice and the number of sides for Peter and Colin's dice.
dice(peter, 9, 4).
dice(colin, 6, 6).

% Predicate to find the probability of getting a total T with N dice each having M sides.
probability(N, M, T, P) :- probability(N, M, T, 0, P).

probability(0, 0, 0, 1).
probability(0, _, _, 0).
probability(N, M, T, S, P) :-
    N > 0,
    M > 0,
    S1 is S + 1,
    N1 is N - 1,
    between(1, M, X),
    T1 is T - X,
    probability(N1, M, T1, S1, P1),
    P is P1 * (1/M).

% Calculate the probability that Pyramidal Peter beats Cubic Colin.
calculate_probability(Result) :-
    dice(peter, NPeter, MPeter),
    dice(colin, NColin, MColin),
    TotalSidesPeter is NPeter * MPeter,
    TotalSidesColin is NColin * MColin,
    (TotalSidesPeter > TotalSidesColin ->
        T is TotalSidesPeter - TotalSidesColin,
        probability(NPeter, MPeter, T, Result)
    ;
        Result is 0
    ).

% Query to calculate the probability.
?- calculate_probability(Probability),
   format('~7f', [Probability]).
