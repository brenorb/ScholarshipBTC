# ScholarshipBTC
`find_range(utxos, x)` finds the timestamp range whose outputs meet `x` with the least excess.
Pass a timestamp-ordered sequence of UTXOs with `amount` and Unix `timestamp` attributes.
Use the same units for `amount` and `x`. The result is `[start, end]`, or `[]` when no range meets `x`.

Done for Jimmy Song's [Programming Blockchain](http://programmingblockchain.com/) seminar.
