=========
FoodFight
=========
------------
A love story
------------

:authors: Daniel Bordak; Chris Lin

About
-----

FoodFight uses Ordr.in's API to pit two friends against each other in a
desperate attempt to not pay for a meal. Whoever wins gets food, whoever loses
has to pay for it.

Note
----

FoodFight requires a Ordr.in Secret Key to be in the envar ORDRIN_API_KEY.
Additionally, Ordr.in's python api library is currently broken in ``pip``.
You need to use the submodule, along with its dependencies (``requests`` and
``jsonschema``).

Also, it doesn't actually order any food, since it's running on test servers,
but it's really the thought that counts.
