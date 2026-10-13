# Python Course: Roadmap and Progress

**Learner:** backend developer (Node.js / TypeScript) starting Python from zero.
**Goal:** expert-level Python for backend services and AI apps (RAG and agents, evenly).
**Pace assumed:** 6-10 h/week, roughly 1-2 modules per week.
**Toolchain:** Python 3.13, uv, pytest, ruff (`uv run pytest -q`, `uv run ruff check . && uv run ruff format .`).

## Overview

| Level | Theme                           | Items   | Est. hours | Est. weeks (at 8 h/wk) |
| ----- | ------------------------------- | ------- | ---------- | ---------------------- |
| 1     | Foundations                     | M01-M07 | ~34        | 4-5                    |
| 2     | Pythonic, typed, tested         | M08-M15 | ~43        | 5-6                    |
| 3     | Advanced Python and concurrency | M16-M22 | ~63        | 8                      |
| 4     | Backend services                | M23-M32 | ~86        | 11                     |
| 5     | AI apps: RAG and agents         | M33-M46 | ~130       | 16                     |
| 6     | Expert                          | M47-M51 | ~79        | 10                     |

Checkpoints: end of Level 2 you are fluent in modern Python. End of Level 4 you can ship a production Python backend. End of Level 5 you can ship RAG and agent services. Hour counts are estimates; adjust as you go.

## Progress tracking

- After each review, update notes/weak_spots.md with the concepts I
  struggled with (one line each, with the date).
- At the start of each session, read README.md and notes/weak_spots.md,
  then tell me where I left off and which weak spot to revisit.
- Every 3 modules, quiz me on earlier weak spots before continuing.

## How this works

- **"Start module N"**: I create `notes/mNN_name.md`, `practice/mNN_name.py` (stubs with `raise NotImplementedError`) and `tests/test_mNN_name.py`. No solutions.
- You fill in the practice file. Ask for a hint (small first, bigger if you ask again).
- **"Review module N"**: I run the tests and review like a senior engineer. I show a reference solution only if you ask.
- Split is about 30% theory, 70% hands-on.
- A module is ticked only when the baseline plus every "Done when" item below it is true.
- **Baseline for every module:** tests green, `ruff check` and `ruff format` clean, type hints on all signatures, review done with no open correctness issues.
- **Mini projects and capstones** are numbered like modules. When they need several files, they use a package folder, `practice/mNN_name/` with `__init__.py`, plus `tests/test_mNN_name.py`. The `pythonpath = ["practice"]` setting in pyproject already supports this.
- Capstones start with a short spec you write in `notes/`. I review the design before you code and the code after.

## Stack defaults

These are my picks. Change any of them before the relevant level starts.

- Web: FastAPI, Pydantic v2, httpx, uvicorn
- Data: Postgres (Docker), SQLAlchemy 2.0, Alembic, Redis
- AI: Anthropic SDK behind a thin provider interface, pgvector, an embeddings provider of your choice, official MCP Python SDK
- Fast-moving libraries (FastAPI, Pydantic, SQLAlchemy, LLM SDKs, MCP, agent frameworks, task queues): **always check the official docs**. Notes will say where.

---

## Level 1: Foundations

Goal: read and write idiomatic basic Python without looking up syntax.

- [ ] **M01 · data_types** · ~5h
  - **Theory:** int/float/Decimal, str and f-strings, bool/None and truthiness, list/tuple/dict/set, slicing, mutable vs immutable, `is` vs `==`, unpacking.
  - **TS bridge:** list ≈ Array, dict ≈ Map (ordered, any hashable key), tuple has no JS equivalent, `None` vs `null`/`undefined`, `[]` is falsy.
  - **Practice:** `word_count` (stub already exists from setup), slicing drills, dict invert/merge, order-preserving dedupe, set algebra, aliasing traps.
  - **Done when:**
    - [ ] All M01 tests pass
    - [ ] You can explain `a = b = []` and shallow vs deep copy with an example
    - [ ] You can pick list/tuple/dict/set for a problem and justify it in one sentence
    - [ ] You can inspect any object in the REPL with `type`, `dir`, `help`, `id`

- [ ] **M02 · control_flow** · ~4h
  - **Theory:** if/elif, `match` (structural pattern matching), for/while, `range`, `enumerate`, `zip`, loop `else`, walrus `:=`.
  - **TS bridge:** indentation instead of braces, `for x in` iterates values (like `for...of`), `a if c else b` instead of `?:`.
  - **Practice:** FizzBuzz variants, text/number parsing, a command dispatcher with `match`, prime sieve, loop-else search.
  - **Done when:**
    - [ ] You rewrote a C-style index loop with `enumerate`/`zip`
    - [ ] You used `match` with sequence, mapping and class patterns
    - [ ] No `range(len(x))` in solutions unless you can justify it

- [ ] **M03 · functions** · ~5h
  - **Theory:** positional/keyword/default args, `*args`/`**kwargs`, keyword-only `*` and positional-only `/`, mutable-default pitfall, LEGB scope, `nonlocal`, closures, first-class functions, lambda, docstrings.
  - **TS bridge:** `**kwargs` ≈ options object, no overloading, defaults are evaluated once (unlike JS), closures capture variables late.
  - **Practice:** flexible-signature utilities, function factories, `sorted(key=...)`, `compose`/`pipe`, fix-the-bug mutable default.
  - **Done when:**
    - [ ] You can explain the mutable-default bug and fix it with a `None` sentinel
    - [ ] You wrote a closure factory and can say exactly what it captures
    - [ ] Every function has a docstring and typed signature

- [ ] **M04 · comprehensions_and_unpacking** · ~4h
  - **Theory:** list/dict/set comprehensions, generator expressions (intro), nested and conditional comprehensions, `*`/`**` unpacking, `sorted`/`min`/`max` with `key`, `any`/`all`, `dict.get`/`setdefault`, `Counter`/`defaultdict` first look.
  - **TS bridge:** replaces `map`/`filter`/`reduce` chains, spread/destructuring, `Object.entries`.
  - **Practice:** reshape lists of dicts (group-by, pivot, flatten, invert), top-N, merge records.
  - **Done when:**
    - [ ] No comprehension is nested more than two levels deep
    - [ ] You implemented group-by three ways (loop, `defaultdict`, comprehension) and can say which you'd pick
    - [ ] You can convert any `map`/`filter` chain from your TS code into idiomatic Python

- [ ] **M05 · modules_and_tooling** · ~4h
  - **Theory:** import system basics, packages and `__init__.py`, absolute vs relative imports, `if __name__ == "__main__"`, `python -m`, uv (`add`/`run`/`sync`/`lock`), `pyproject.toml`, pytest basics, ruff, `breakpoint()` and pdb.
  - **TS bridge:** uv ≈ npm + nvm, `pyproject.toml` ≈ `package.json`, `uv.lock` ≈ lockfile, ruff ≈ eslint + prettier, pytest ≈ jest/vitest.
  - **Practice:** split a messy single file into a package, fix a circular import, add a dependency and use it, write a `__main__` entry point, debug with pdb.
  - **Done when:**
    - [ ] A fresh clone works with `uv sync` then `uv run pytest -q`
    - [ ] You can explain why `python file.py` and `python -m pkg.mod` resolve imports differently
    - [ ] You stepped through a bug with pdb

- [ ] **M06 · errors_and_files** · ~5h
  - **Theory:** exception hierarchy, try/except/else/finally, `raise ... from`, custom exceptions, EAFP vs LBYL, `with`, `pathlib`, text vs binary I/O and encodings, `json`, `csv`, `logging` basics, `tmp_path`.
  - **TS bridge:** typed catch by class, `with` ≈ try/finally (or `using`), `pathlib` ≈ `path` + `fs`.
  - **Practice:** robust config loader, JSON/CSV read-transform-write with error reporting, custom exception hierarchy, log parser.
  - **Done when:**
    - [ ] No bare `except:` and no swallowed exceptions
    - [ ] All file access uses `with` and `pathlib`
    - [ ] You can explain `raise ... from e` and when to use it

- [ ] **M07 · MINI: cli_notes** · ~7h
  - **Build:** a notes/todo CLI with subcommands (add, list, done, rm, search), JSON storage, logging. Use argparse (or typer; check docs).
  - **Done when:**
    - [ ] All subcommands work and data survives restarts
    - [ ] Bad input gives a friendly message and a non-zero exit code
    - [ ] At least 10 tests using `tmp_path` and `capsys`
    - [ ] Usage documented in `notes/m07_cli_notes.md`

**Level 1 gate**

- [ ] All Level 1 items ticked
- [ ] From a blank file you can write a script that reads CSV/JSON, aggregates with comprehensions, handles errors and writes output, with no copy-paste
- [ ] You can read a 100-line Python script you didn't write and explain it

---

## Level 2: Pythonic, typed, tested

Goal: write code a senior Python reviewer would accept.

- [ ] **M08 · type_hints** · ~5h
  - **Theory:** built-in generics (`list[int]`), `X | None`, `Callable`, PEP 695 generics syntax, `Literal`, `TypedDict`, `Protocol`, `Final`, `Self`, `Any` vs `object`, static vs runtime (hints are not enforced). Add a type checker (pyright or mypy; check docs) as a dev dependency.
  - **TS bridge:** gradual typing like TS, but erased and unchecked at runtime. `Protocol` ≈ structural interfaces.
  - **Practice:** annotate an untyped module until the checker is clean, write generic `first()` and `Stack[T]`, define a `Protocol` plugin interface, fix a file full of type errors.
  - **Done when:**
    - [ ] The type checker (strict mode) reports 0 errors on all Level 2 practice files
    - [ ] No unjustified `Any` or `# type: ignore`
    - [ ] You can explain why hints don't validate data at runtime

- [ ] **M09 · classes_and_oop** · ~6h
  - **Theory:** class vs instance attributes, `classmethod`/`staticmethod`, dunder methods (`__repr__`, `__eq__`, `__hash__`, `__lt__`, `__iter__`, `__len__`, `__contains__`), properties, inheritance and MRO, `super()`, composition over inheritance, ABC vs Protocol.
  - **TS bridge:** no `private` keyword (`_name` convention), properties ≈ getters/setters, multiple inheritance exists, duck typing.
  - **Practice:** `Money`/`Vector` value type with operators, `LRUCache` container with dunder protocols, refactor an inheritance tree to composition.
  - **Done when:**
    - [ ] You built a container that works with `len`, `in`, `for` and `[]`
    - [ ] You can explain MRO on a diamond hierarchy
    - [ ] You can state the `__eq__`/`__hash__` contract
    - [ ] You justified one inheritance-vs-composition decision in notes

- [ ] **M10 · dataclasses_and_enums** · ~4h
  - **Theory:** `@dataclass` (`frozen`, `slots`, `order`, `kw_only`, `default_factory`, `__post_init__`), `NamedTuple`, `Enum`/`StrEnum`/`Flag`, `dataclasses.replace`.
  - **TS bridge:** dataclass ≈ interface + constructor, `frozen` ≈ `readonly`, `StrEnum` ≈ string-literal union.
  - **Practice:** order/inventory domain model with validation, dict round-tripping, state machine with Enum transitions, frozen value objects as dict keys.
  - **Done when:**
    - [ ] Notes contain a decision table: dataclass vs NamedTuple vs TypedDict vs plain class
    - [ ] You can explain the mutable-default error in dataclasses and its `default_factory` fix

- [ ] **M11 · iterators_and_generators** · ~5h
  - **Theory:** iterable vs iterator, `__iter__`/`__next__`, `yield`, `yield from`, generator expressions, laziness and memory, `itertools` (`chain`, `islice`, `groupby`, `batched`, `accumulate`, `product`).
  - **TS bridge:** like `function*` and `for...of`, but idiomatic everywhere.
  - **Practice:** custom iterator class, chunked file reader, sliding window, lazy pipeline over a huge stream.
  - **Done when:**
    - [ ] A stream pipeline runs in constant memory (shown with `tracemalloc` or a test)
    - [ ] You can explain iterator exhaustion with an example

- [ ] **M12 · decorators_and_context_managers** · ~5h
  - **Theory:** decorators with and without args, `functools.wraps`, `cache`/`lru_cache`, stacking order, `contextlib.contextmanager`, `__enter__`/`__exit__`, `ExitStack`, `suppress`.
  - **TS bridge:** higher-order function wrappers (not TS class decorators). FastAPI uses these constantly.
  - **Practice:** `@timed`, `@retry(n, exceptions)`, `@memoize`, timer/temp-dir/transaction context managers.
  - **Done when:**
    - [ ] Decorators preserve name, docstring and signature
    - [ ] You wrote one context manager both class-based and generator-based
    - [ ] You can explain what `@deco` desugars to

- [ ] **M13 · testing_with_pytest** · ~5h
  - **Theory:** fixtures (scope, `yield` teardown), `conftest.py`, `parametrize`, marks, `tmp_path`, `monkeypatch`, `capsys`, `unittest.mock`, `pytest.raises`, coverage (`pytest-cov`), Hypothesis (intro), arrange-act-assert, the TDD loop.
  - **TS bridge:** like jest/vitest, but fixtures (dependency injection) replace `beforeEach`, `parametrize` ≈ `test.each`.
  - **Practice:** you write the tests for a provided module that has seeded bugs; every bug must be caught, then fix them.
  - **Done when:**
    - [ ] At least 90% line coverage on the target module with meaningful assertions
    - [ ] You used a fixture, `parametrize`, `monkeypatch` and `raises` at least once each
    - [ ] One Hypothesis property test guards an edge case

- [ ] **M14 · stdlib_toolkit** · ~5h
  - **Theory:** `collections` (`deque`, `Counter`, `defaultdict`, `ChainMap`), `functools` (`partial`, `singledispatch`, `cached_property`), `datetime`/`zoneinfo` (aware vs naive), `re`, `secrets`/`hashlib`/`hmac`, `subprocess`, `heapq`/`bisect`, `uuid`, `decimal`, `sqlite3`.
  - **TS bridge:** batteries included replaces lodash, uuid, crypto and much of date-fns.
  - **Practice:** timezone-aware schedule math, regex log extraction, `deque` rate limiter, HMAC signer, sqlite3 CRUD wrapper, safe `subprocess.run`.
  - **Done when:**
    - [ ] All datetimes in solutions are timezone-aware
    - [ ] You scored at least 80% on the "which stdlib tool?" quiz in the notes

- [ ] **M15 · MINI: expense_tracker_lib** · ~8h
  - **Build:** a typed library plus small CLI. Dataclasses and enums for the domain, generator-based report streaming, a decorator for logging/timing, storage behind a `Protocol` (JSON and sqlite3 backends).
  - **Done when:**
    - [ ] Storage backend swaps without touching core code, with a test that proves it
    - [ ] At least 90% coverage, type checker strict-clean, ruff clean
    - [ ] Reports stream lazily (no full-list materialization)

**Level 2 gate**

- [ ] All Level 2 items ticked
- [ ] From memory, you can implement an iterator, a context manager, a decorator with args, a dataclass and a Protocol
- [ ] Your last two modules got review comments only on style, not correctness

---

## Level 3: Advanced Python and concurrency

Goal: understand how Python works under the hood and write correct concurrent code.

- [ ] **M16 · data_model_deep_dive** · ~6h
  - **Theory:** `__getattr__`/`__getattribute__`/`__setattr__`, descriptors, `__slots__`, `__call__`, `__init_subclass__`, metaclasses (and why you rarely need one), `abc`, `weakref`, refcounting plus cyclic GC, interning, copy semantics.
  - **TS bridge:** `Proxy`/`Reflect` ≈ `__getattr__`/descriptors, prototypes vs classes, deterministic refcount vs V8 GC.
  - **Practice:** write your own `cached_property`, validated-field descriptors, plugin registry via `__init_subclass__`, `weakref` cache, observe a GC cycle.
  - **Done when:**
    - [ ] You implemented a `property`-equivalent descriptor from scratch
    - [ ] You can explain refcount vs cyclic GC and why `__del__` is a trap
    - [ ] You can say when to use a metaclass, `__init_subclass__` or a decorator

- [ ] **M17 · concurrency_threads_processes** · ~6h
  - **Theory:** what the GIL does and doesn't do, I/O-bound vs CPU-bound, `threading`, locks, `queue.Queue`, race conditions, `concurrent.futures`, `multiprocessing` (pickling, start methods), experimental free-threaded build and JIT in 3.13 (check current docs).
  - **TS bridge:** Node is a single-threaded loop plus `worker_threads`. `ProcessPoolExecutor` ≈ worker pool.
  - **Practice:** threaded downloader, CPU-bound threads-vs-processes benchmark, thread-safe counter, producer/consumer queue, fix a deadlock.
  - **Done when:**
    - [ ] Benchmark numbers in notes show threads win for I/O and processes win for CPU-bound work
    - [ ] You reproduced a race condition and fixed it
    - [ ] Notes contain a threads vs processes vs asyncio decision guide

- [ ] **M18 · asyncio_core** · ~7h
  - **Theory:** coroutines, event loop, tasks, `gather` vs `TaskGroup`, `asyncio.timeout`, cancellation, `Semaphore`/`Lock`/`Queue`/`Event`, async iterators and generators, async context managers, `to_thread`, `ExceptionGroup`/`except*`, testing async code (check docs for `pytest-asyncio` vs anyio).
  - **TS bridge:** closest mapping to your Node knowledge. Tasks ≈ Promises, `TaskGroup` ≈ `Promise.all` with structured cleanup. But coroutines are lazy until awaited or scheduled, and cancellation is real.
  - **Practice:** concurrent fetch simulator, rate-limited worker pool, timeout and cancel handling, async stream, fan-out/fan-in with queues, fix a blocking call in a coroutine.
  - **Done when:**
    - [ ] You used `TaskGroup` and handled `ExceptionGroup`
    - [ ] You cancelled a task cleanly, with cleanup in `finally`
    - [ ] You can explain why `time.sleep` in a coroutine stalls everything, and fix it with `to_thread`

- [ ] **M19 · performance_and_profiling** · ~5h
  - **Theory:** `timeit`, `cProfile`/`pstats`, `tracemalloc`, py-spy or scalene (check docs), complexity and data-structure choice, `lru_cache`, `__slots__`, string-building pitfalls, numpy preview, when to drop to C/Rust.
  - **TS bridge:** V8 is faster on pure loops. Python wins through C-backed libraries.
  - **Practice:** optimize provided slow functions (N² to N log N, caching), profile a deliberately slow program and fix the top hotspot.
  - **Done when:**
    - [ ] Notes include before/after profiler output for at least 3 optimizations
    - [ ] Tests carry generous performance budgets
    - [ ] You can demonstrate "measure first" on a case where the obvious fix was wrong

- [ ] **M20 · packaging_and_distribution** · ~5h
  - **Theory:** src layout, `pyproject.toml` metadata/extras/entry points, wheels vs sdist, SemVer, `uv build`/`uv publish`, TestPyPI, `py.typed`, `__all__`, public API design, pre-commit, GitHub Actions (lint, test, matrix).
  - **TS bridge:** entry points ≈ `bin`, PyPI ≈ npm, extras ≈ optional peer deps.
  - **Practice:** package a utility from earlier modules with a CLI entry point, build it, install into a clean venv, add a CI workflow file.
  - **Done when:**
    - [ ] `uv build` produces wheel and sdist, and the entry point works from a clean venv
    - [ ] Public API is explicit (`__all__`, `py.typed`)
    - [ ] A CI workflow is committed (green if the repo has a GitHub remote)

- [ ] **M21 · MINI: async_fetcher** · ~6h
  - **Build:** a CLI that fetches many URLs concurrently with `httpx.AsyncClient`. Concurrency limit, timeouts, retries with exponential backoff and jitter, per-host rate limiting, JSON results. Tests use `httpx.MockTransport`, no real network.
  - **Done when:**
    - [ ] A test asserts max in-flight requests never exceeds the limit
    - [ ] Failures are retried then reported, never crash the run
    - [ ] Ctrl+C cancels cleanly
    - [ ] Type checker and ruff clean

- [ ] **M22 · CAPSTONE 1: jobq (async job-queue library)** · ~28h
  - **Build:** an in-process async job queue. Workers with configurable concurrency, priorities, retries with backoff, timeouts, cancellation, graceful shutdown, storage behind a `Protocol` (memory and sqlite), generic typed API, `@job` registration decorator, metrics hooks, small inspection CLI.
  - **Done when:**
    - [ ] You wrote a spec in `notes/` (API, failure modes) before coding, and I reviewed it
    - [ ] All features above work
    - [ ] At least 90% coverage, with race and cancellation tests and a Hypothesis test on ordering invariants
    - [ ] Type checker strict-clean, ruff clean
    - [ ] Benchmark with jobs/sec and a profile recorded in notes
    - [ ] Wheel builds and an example script runs from a clean venv
    - [ ] Two review rounds done (design, then code)

**Level 3 gate**

- [ ] All Level 3 items ticked
- [ ] You can explain the GIL, the event loop and when to pick threads, processes or asyncio, without notes
- [ ] You can profile a slow Python program and show where the time goes

---

## Level 4: Backend services

Goal: build, secure, deploy and observe production-style Python APIs.

- [ ] **M23 · http_and_pydantic** · ~6h
  - **Theory:** HTTP refresher (methods, status codes, idempotency), `httpx` sync/async, timeouts and retries, Pydantic v2 (`BaseModel`, `Field`, `field_validator`, `model_validator`, aliases, discriminated unions, `TypeAdapter`, JSON Schema), `pydantic-settings`. Check the official Pydantic v2 docs.
  - **TS bridge:** Pydantic ≈ zod plus TS types in one. httpx ≈ axios/fetch. Settings ≈ dotenv plus zod env parsing.
  - **Practice:** typed API client, nested model validation with readable errors, settings from env/.env, discriminated-union event parser.
  - **Done when:**
    - [ ] Invalid payloads produce structured, readable errors (shown in a test)
    - [ ] No raw dicts cross function boundaries in your solutions
    - [ ] Settings fail fast on invalid or missing env vars

- [ ] **M24 · fastapi_fundamentals** · ~6h
  - **Theory:** ASGI vs WSGI, uvicorn, path/query/body params, response models, status codes, `HTTPException`, exception handlers, `Depends`, routers, OpenAPI, `def` vs `async def` endpoints. Check the official FastAPI docs.
  - **TS bridge:** Express/Fastify + zod + OpenAPI in one, `Depends` ≈ Nest providers.
  - **Practice:** in-memory CRUD API with typed models, pagination and filters, custom error format, current-user dependency stub, `TestClient` tests.
  - **Done when:**
    - [ ] `/docs` documents every endpoint including error responses
    - [ ] No endpoint returns an un-modeled dict
    - [ ] You can explain when to use `def` vs `async def` endpoints

- [ ] **M25 · sql_and_sqlalchemy** · ~7h
  - **Theory:** joins, indexes, transactions and isolation, N+1, SQLAlchemy 2.0 (`Mapped[]`, relationships, session/unit of work, async engine), Alembic, connection pooling, Postgres via Docker Compose, repository pattern intro. Check the official SQLAlchemy docs.
  - **TS bridge:** Core ≈ query builder (Drizzle/knex), ORM ≈ TypeORM/Prisma, Alembic ≈ Prisma Migrate.
  - **Practice:** blog or orders schema, migrations (create, alter, data), joins/aggregation/upsert, reproduce and fix N+1, transactional transfer with rollback test.
  - **Done when:**
    - [ ] Schema changes only through Alembic, and both upgrade and downgrade work
    - [ ] N+1 reproduced and fixed, with query count asserted in a test
    - [ ] You can explain the session lifecycle, `flush` vs `commit`

- [ ] **M26 · auth_and_security** · ~6h
  - **Theory:** password hashing (argon2/bcrypt), sessions vs JWT, OAuth2 bearer flow in FastAPI, refresh tokens, API keys, RBAC/scopes, CORS, rate limiting, SQL injection, secrets handling, OWASP API Top 10. Check docs; recommended auth libraries change.
  - **TS bridge:** passport/jose ≈ PyJWT and a hashing lib.
  - **Practice:** register/login/refresh endpoints, protected routes via dependency, roles, rate limiting, security tests (expired, tampered, wrong role).
  - **Done when:**
    - [ ] A test asserts passwords are never stored or logged in plaintext
    - [ ] Tests prove tampered and expired JWTs are rejected
    - [ ] Notes review your API against the OWASP API Top 10

- [ ] **M27 · MINI: bookmarks_api** · ~8h
  - **Build:** FastAPI + Postgres (SQLAlchemy, Alembic) + JWT auth. Users own bookmarks, tags, search, pagination. Docker Compose for the DB.
  - **Done when:**
    - [ ] A test proves user A cannot read or edit user B's bookmarks
    - [ ] At least 85% coverage, with isolated DB state per test
    - [ ] Runs from a clean clone with `docker compose up` and `uv run`
    - [ ] OpenAPI is clean and complete

- [ ] **M28 · fastapi_in_depth** · ~7h
  - **Theory:** lifespan, middleware, dependency overrides in tests, background tasks, streaming and SSE, WebSockets, file uploads, cursor vs offset pagination, idempotency keys, API versioning, problem-details errors (RFC 9457), async DB sessions per request, async test client.
  - **TS bridge:** Express middleware chain, Nest guards/interceptors/filters.
  - **Practice:** a small standalone app (or extend bookmarks_api): cursor pagination, SSE events, request-ID middleware, problem+json errors, webhook via background task, async test suite.
  - **Done when:**
    - [ ] Dependency overrides test the app without external services
    - [ ] SSE streams events and handles client disconnect
    - [ ] One consistent error format across all failure paths

- [ ] **M29 · redis_queues_caching** · ~6h
  - **Theory:** Redis data structures, cache-aside, TTL and stampede protection, rate limiting, task queues (Celery, RQ, Dramatiq, arq; pick one and check its maintenance status), at-least-once delivery, idempotent jobs, retries and dead-letter queues, scheduling.
  - **TS bridge:** BullMQ ≈ Celery/RQ workers, ioredis ≈ redis-py.
  - **Practice:** cache-aside decorator with invalidation, sliding-window rate limiter, background worker with retries and DLQ, idempotency-key store.
  - **Done when:**
    - [ ] A test shows a job processed twice yields the same result
    - [ ] A failing job lands in the DLQ after N retries
    - [ ] You can explain and demo cache-stampede mitigation

- [ ] **M30 · observability_and_config** · ~5h
  - **Theory:** 12-factor config, structured JSON logging with correlation IDs, Prometheus metrics, OpenTelemetry traces, `/healthz` vs `/readyz`, log hygiene and PII. Check OpenTelemetry docs.
  - **TS bridge:** pino ≈ structlog or JSON stdlib logging, prom-client ≈ prometheus_client, OTel JS ≈ OTel Python.
  - **Practice:** JSON logging with request IDs, health/readiness endpoints with DB check, latency histogram per route, traces to console or Jaeger, per-environment settings.
  - **Done when:**
    - [ ] One request is traceable by a single correlation ID across all its logs
    - [ ] Metrics expose request count and latency by route
    - [ ] Readiness fails when the DB is down (tested)
    - [ ] No secrets or PII in logs (tested or linted)

- [ ] **M31 · docker_and_ci** · ~5h
  - **Theory:** multi-stage Docker builds with uv, slim non-root images, layer caching, Compose (app, Postgres, Redis, worker), uvicorn/gunicorn workers, SIGTERM and graceful shutdown, healthchecks, GitHub Actions (lint, type check, test with services, build image), deployment targets overview.
  - **TS bridge:** `uv sync --frozen` ≈ `npm ci`. Everything else carries over.
  - **Practice:** containerize bookmarks_api, Compose with DB + Redis + app + worker, CI pipeline with caching, migrations on deploy, smoke-test script.
  - **Done when:**
    - [ ] `docker compose up` brings the full stack healthy from a clean clone
    - [ ] Image is slim, non-root, and its size is recorded in notes
    - [ ] CI runs ruff, type checker and pytest with services, and builds the image
    - [ ] An in-flight request completes on SIGTERM

- [ ] **M32 · CAPSTONE 2: ticketing_service** · ~30h
  - **Build:** a multi-tenant support-ticket service. Orgs, users and roles, tickets with comments, search and filters, notifications via background jobs and webhooks, audit log, rate limits, observability, Docker Compose, CI. (Pick a different domain if you prefer; same requirements.)
  - **Done when:**
    - [ ] Spec and at least 2 ADRs written and reviewed before coding
    - [ ] Tenant-isolation tests prove org A can never see org B's data
    - [ ] At least 85% coverage, type checker and ruff clean
    - [ ] Load-test report (Locust or k6) with p95 recorded, plus one bottleneck found and fixed
    - [ ] Clean-clone `docker compose up` works and CI is green
    - [ ] Security checklist and a runbook section in the README
    - [ ] Two review rounds done (design, then code)

**Level 4 gate**

- [ ] All Level 4 items ticked
- [ ] Within about one working day you can scaffold, test, containerize and deploy-ready a small CRUD service from an empty directory, without copy-paste

---

## Level 5: AI apps (RAG and agents)

Goal: build reliable, testable, observable LLM features, not demos.

- [ ] **M33 · data_tools** · ~5h
  - **Theory:** numpy arrays, dtype, broadcasting, vectorization, dot product/norms/cosine similarity, `argsort`/top-k, DataFrames with polars or pandas (pick one; check docs), JSONL datasets.
  - **TS bridge:** no good JS equivalent. Think typed arrays plus lodash, but vectorized.
  - **Practice:** top-k cosine search by loop and by numpy, clean a Q&A dataset, p50/p95/p99 from a request log, JSONL load/save.
  - **Done when:**
    - [ ] Vectorized top-k is at least 10x faster than the loop (numbers in notes)
    - [ ] You can explain broadcasting with two examples
    - [ ] You can compute latency percentiles from a log file

- [ ] **M34 · llm_api_fundamentals** · ~6h
  - **Theory:** messages API, roles, system prompts, tokens/context/cost, sampling params, stop reasons, streaming, timeouts/retries/rate limits (429, overloaded), prompt caching, multi-turn state (you resend history), model choice by cost/latency/quality, sync vs async client, key hygiene. SDKs and models change fast: check the official docs.
  - **TS bridge:** the TS and Python SDKs have near-identical shape.
  - **Practice:** thin `LLMClient` wrapper with retries, timeouts and usage/cost logging, streaming printer, multi-turn loop with history truncation, token-budget estimator, tests with a fake client.
  - **Done when:**
    - [ ] Tests need no network and no API key
    - [ ] The API key comes only from env/settings and is never committed
    - [ ] The wrapper reports usage and cost per call
    - [ ] You can explain why the API is stateless

- [ ] **M35 · structured_outputs_and_prompts** · ~5h
  - **Theory:** prompts as versioned code, few-shot, structured output via tool-use or JSON schema plus Pydantic validation, bounded repair/retry on invalid output, extraction and classification patterns, prompt-injection basics, recorded-response fixtures for tests.
  - **TS bridge:** same pattern as zod-validated LLM output.
  - **Practice:** text-to-Pydantic extractor with retry, enum classifier, prompt template registry, golden-fixture tests.
  - **Done when:**
    - [ ] Every model output entering your app is a validated Pydantic model
    - [ ] Validation failure triggers a bounded, logged retry
    - [ ] Prompts live in versioned files, not inline strings

- [ ] **M36 · embeddings_and_vector_search** · ~6h
  - **Theory:** what embeddings are, similarity metrics, chunking (size/overlap/structure-aware), hosted vs local embedding models, pgvector, HNSW vs IVFFlat tradeoffs, metadata filters, hybrid search preview.
  - **TS bridge:** same concepts. Python's ecosystem is deepest here.
  - **Practice:** chunker with boundary/unicode tests, in-memory numpy index, pgvector store behind the same `Protocol`, markdown-folder ingestion, filtered queries.
  - **Done when:**
    - [ ] In-memory and pgvector stores pass the same test suite via one `Protocol`
    - [ ] Chunker properties are tested (no text lost, overlap invariant)
    - [ ] You can explain the recall/latency tradeoff of HNSW parameters

- [ ] **M37 · rag_pipeline** · ~6h
  - **Theory:** ingest, chunk, embed, store, retrieve, rerank, assemble prompt, generate, cite. Context budgeting, grounding and "I don't know", query rewriting, hybrid search and reranking, index freshness, common failure modes.
  - **TS bridge:** LangChain.js and LlamaIndex.TS exist. Build from scratch first, compare frameworks afterwards.
  - **Practice:** pluggable pipeline, token-budgeted context assembler, citation extraction and validation, no-answer path, fake LLM for deterministic tests.
  - **Done when:**
    - [ ] Every answer's citations map to real retrieved chunks, checked in code
    - [ ] An out-of-scope question takes the refusal path (tested)
    - [ ] You can name and demo 3 RAG failure modes

- [ ] **M38 · MINI: docs_qa_cli** · ~6h
  - **Build:** CLI `ask "question"` over a local markdown folder. Ingest command, hash-based incremental re-ingest, answers with citations and source paths, streamed output.
  - **Done when:**
    - [ ] Re-running ingest on unchanged files does nothing
    - [ ] A changed file is re-indexed alone
    - [ ] At least 10 tests using fakes
    - [ ] Works end-to-end on your own `notes/` folder (demonstrated)

- [ ] **M39 · rag_evaluation** · ~6h
  - **Theory:** golden datasets, recall@k, MRR, nDCG, faithfulness/relevance/correctness, LLM-as-judge pitfalls (bias, position, cost), CI regression gates, error-analysis loop, eval frameworks overview (check docs).
  - **TS bridge:** like integration tests, but statistical, with thresholds.
  - **Practice:** a 30-50 question golden set from your notes, retrieval metrics, an LLM judge with a rubric calibrated against your labels, config comparison with numbers.
  - **Done when:**
    - [ ] Golden set has at least 30 questions with labeled relevant chunks
    - [ ] A report compares at least 2 configurations by recall@k and MRR
    - [ ] Judge agreement with your manual labels is measured
    - [ ] The eval runs in CI in cached or fake mode

- [ ] **M40 · ai_in_production** · ~6h
  - **Theory:** SSE token streaming from FastAPI, concurrency limits and backpressure, provider rate limits, retries and model fallbacks, response caching, cost tracking and budgets, LLM tracing (OTel, Langfuse/Phoenix; check docs), prompt injection and data exfiltration, PII redaction, degraded modes.
  - **TS bridge:** same infrastructure ideas. Compare the Vercel AI SDK stream protocol with raw SSE.
  - **Practice:** SSE chat endpoint with disconnect cancellation, concurrency limiter, per-user token budget, prompt-injection test suite, PII redactor, fallback to a secondary model (fakes).
  - **Done when:**
    - [ ] A client disconnect cancels the upstream LLM call (tested)
    - [ ] Exceeding the budget returns 429 with a clear error
    - [ ] Injection suite has at least 5 documented attacks with outcomes
    - [ ] Traces show latency and tokens per LLM call

- [ ] **M41 · CAPSTONE 3: rag_service** · ~30h
  - **Build:** RAG as a service. FastAPI + Postgres/pgvector, async ingestion worker (upload, chunk, embed), multi-tenant collections, hybrid retrieval, streamed answers with citations, auth, eval harness, observability, Docker Compose.
  - **Done when:**
    - [ ] Spec, architecture diagram and ADRs reviewed before coding
    - [ ] Ingest, query, delete and reindex endpoints work
    - [ ] A test proves tenant A never retrieves tenant B's chunks
    - [ ] Streamed answers carry validated citations
    - [ ] CI gates on eval thresholds (recall@k, faithfulness) you chose and justified
    - [ ] Tracing and cost visibility in place
    - [ ] Clean-clone `docker compose up` works, retrieval p95 recorded under load
    - [ ] Two review rounds done (design, then code)

- [ ] **M42 · tool_use_and_function_calling** · ~5h
  - **Theory:** tool schemas from Pydantic/type hints, tool_use/tool_result message flow, parallel tool calls, tool choice, returning errors to the model, tool design (small, typed, idempotent, descriptive errors), read vs write tools, permissions and sandboxing. Check the provider's tool-use docs.
  - **TS bridge:** zod to JSON Schema is the same idea, and the Vercel AI SDK `tool()` ≈ the registry you'll build.
  - **Practice:** `@tool` registry that derives schemas from type hints, dispatch loop with max iterations, tools (calculator, sandboxed file reader, allowlisted HTTP GET, read-only SQL), scripted fake model for tests.
  - **Done when:**
    - [ ] Schemas are generated from type hints, not hand-written
    - [ ] Tool errors go back to the model and never crash the loop
    - [ ] The loop has a hard iteration cap and timeout (tested)
    - [ ] Write-capable tools require a confirmation hook

- [ ] **M43 · MINI: tool_assistant_cli** · ~6h
  - **Build:** a CLI assistant with at least 3 tools, conversation memory, streamed output, printed tool-call trace, per-run budget.
  - **Done when:**
    - [ ] Scripted fake-model tests cover multi-tool turns and tool failures
    - [ ] Budget and iteration limits stop a runaway loop (tested)
    - [ ] You used it for a real task and noted what broke

- [ ] **M44 · agents_from_scratch** · ~7h
  - **Theory:** agent loop, planning (ReAct, plan-then-execute), short- and long-term memory, state machines, guardrails, human-in-the-loop, resumable long-running runs, multi-agent tradeoffs, workflows vs agents, framework landscape (Claude Agent SDK, LangGraph and others; check docs).
  - **TS bridge:** XState-style state machines, LangGraph.js vs LangGraph Python.
  - **Practice:** pluggable agent loop with step and cost budgets, persisted run state with resume after a crash, planner/executor split, approval checkpoint, trace recorder with deterministic replay.
  - **Done when:**
    - [ ] A run killed mid-way resumes from persisted state (tested)
    - [ ] Replaying a recorded run reproduces the final result
    - [ ] Notes explain when you'd use a plain workflow instead of an agent

- [ ] **M45 · mcp_servers** · ~6h
  - **Theory:** Model Context Protocol (tools, resources, prompts), stdio vs streamable HTTP transports, the Python SDK (FastMCP), designing tools for LLMs, testing servers, security (tool poisoning, least privilege). The spec evolves: check the official docs.
  - **TS bridge:** the TS and Python SDKs speak the same protocol.
  - **Practice:** MCP server exposing notes search (from docs_qa), a read-only DB tool and a resource. Test with an in-memory client, connect it to Claude Code, add an HTTP-transport variant.
  - **Done when:**
    - [ ] The server works from Claude Code (demo captured in notes)
    - [ ] Every tool has a typed schema, docstring and error handling
    - [ ] Read-only and write tools are separated, least privilege documented

- [ ] **M46 · CAPSTONE 4: agent_service** · ~30h
  - **Build:** a service for long-running agent tasks. `POST /runs` starts a task, events stream over SSE, `GET /runs/{id}` returns status. Tools include your MCP server. Resumable runs, budgets, allowlists, human approval for writes, tracing, auth, Docker Compose.
  - **Done when:**
    - [ ] Spec and threat model reviewed before coding
    - [ ] Killing the worker mid-run resumes the run (tested)
    - [ ] Write actions require approval, with a test for the denial path
    - [ ] Eval suite of at least 20 scripted scenarios (fake or recorded tools) reports success rate in CI
    - [ ] Per-run cost and step budgets enforced
    - [ ] Traces show every tool call and model call
    - [ ] Clean-clone `docker compose up` works
    - [ ] Two review rounds done (design, then code)

**Level 5 gate**

- [ ] All Level 5 items ticked
- [ ] You can explain RAG vs fine-tuning vs agents vs plain workflows and defend a choice for a given problem
- [ ] You have eval numbers (not vibes) for both your RAG and agent services

---

## Level 6: Expert

Goal: design well, go deep on internals, and contribute outward.

- [ ] **M47 · architecture_and_patterns** · ~7h
  - **Theory:** layering and hexagonal architecture without over-engineering, dependency injection without a framework, repository and unit of work, domain events, modular monolith vs microservices, ADRs, error-handling strategy, API evolution, Pythonic anti-patterns (Java-isms), uv workspaces.
  - **TS bridge:** Nest modules vs FastAPI composition. Python prefers functions and modules over deep class hierarchies.
  - **Practice:** refactor ticketing_service into ports and adapters, in-memory adapters for fast tests, write 3 ADRs.
  - **Done when:**
    - [ ] The domain layer imports nothing from FastAPI or SQLAlchemy (enforced by test or import-linter)
    - [ ] The domain test suite runs in under 1s with no I/O
    - [ ] 3 ADRs with explicit tradeoffs

- [ ] **M48 · advanced_typing_and_metaprogramming** · ~7h
  - **Theory:** `ParamSpec`, `Concatenate`, `TypeVarTuple`, `overload`, generic `Protocol`, `TypeGuard`/`TypeIs`, `Annotated`, variance, `inspect`, `get_type_hints`, `ast`, metaclass use cases, how FastAPI and Pydantic build on type hints. Check the docs for 3.14 changes (deferred annotations, t-strings).
  - **TS bridge:** no conditional or mapped types, but Python types are readable at runtime.
  - **Practice:** a fully typed signature-preserving decorator, a type-hint-driven DI container, a mini validation lib on `Annotated`, a tiny FastAPI-like router, an AST-based lint rule.
  - **Done when:**
    - [ ] Strict type checker passes and `reveal_type` shows signatures preserved
    - [ ] Your mini-router parses path, query and body from function signatures
    - [ ] You can explain how FastAPI uses `Annotated` and `inspect`

- [ ] **M49 · scaling_and_performance** · ~7h
  - **Theory:** load testing, py-spy under load, `EXPLAIN ANALYZE`, indexes and pool sizing, worker configuration, caching layers, backpressure, queue-based load leveling, stateless horizontal scaling, percentiles, free-threading and JIT status (check docs), PyO3/Cython (demo only).
  - **Practice:** load-test the ticketing and RAG services, fix the top 3 bottlenecks using data, tune pool and worker sizes, add a cache with measured hit rate, write a performance report.
  - **Done when:**
    - [ ] Report shows before/after p95 and throughput for 3 optimizations
    - [ ] Pool and worker sizes are justified by measurements
    - [ ] Under overload the service degrades gracefully (429/503 with `Retry-After`)

- [ ] **M50 · internals_and_open_source** · ~8h
  - **Theory:** bytecode and `dis`, frames and the eval loop, refcounting and GC, import machinery, `sys.monitoring`/`settrace` (check docs), reading stdlib and library source, contribution workflow (repro, PR conventions, tests).
  - **Practice:** disassemble and explain 5 snippets, write a small tracer or profiler, read one library path end-to-end and write it up, submit one upstream PR (docs, test or bugfix).
  - **Done when:**
    - [ ] Notes explain how a request travels through Starlette/FastAPI to your handler
    - [ ] The tracer has tests
    - [ ] One upstream PR submitted (link in notes)

- [ ] **M51 · CAPSTONE 5 (final): your own product** · ~50h
  - **Build:** a real problem you or your team would use. Backend service plus AI (RAG, agents or both) plus production concerns, using everything above.
  - **Done when:**
    - [ ] One-page spec, success metrics and threat model reviewed before coding
    - [ ] Reachable deployment, or one-command Compose, with CI/CD
    - [ ] At least 85% coverage, and an eval suite with thresholds gating CI
    - [ ] Logs, metrics and traces in place, plus a runbook
    - [ ] Load-test report and security checklist
    - [ ] README, ADRs and a 10-minute demo walkthrough
    - [ ] Final review asks "would I approve this PR and ship this?" and the answer is yes

**Level 6 gate (graduation)**

- [ ] All Level 6 items ticked
- [ ] You can design a Python service from scratch and defend each tradeoff
- [ ] You can debug performance with profilers and read CPython bytecode
- [ ] You can review someone else's Python code and catch correctness, style and design issues
- [ ] You keep up with fast-moving libraries by reading the official docs

---

## Optional electives

Pick up after Level 4 or 5 if relevant.

- [ ] Django or Flask comparison: rebuild bookmarks_api, write down tradeoffs vs FastAPI
- [ ] GraphQL (Strawberry) over an existing service
- [ ] Fine-tuning or local-model serving basics (vLLM/Ollama)
- [ ] Rust extension with PyO3 for one hot path
- [ ] Kubernetes deployment of the capstone services
