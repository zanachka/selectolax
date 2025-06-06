from typing import Any, Iterator, Literal, TypeVar, NoReturn, overload

DefaultT = TypeVar("DefaultT")

class LexborAttributes:
    @staticmethod
    def create(node: LexborAttributes) -> LexborAttributes: ...
    def keys(self) -> Iterator[str]: ...
    def items(self) -> Iterator[tuple[str, str | None]]: ...
    def values(self) -> Iterator[str | None]: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: str) -> str | None: ...
    def __setitem__(self, key: str, value: str) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __contains__(self, key: str) -> bool: ...
    def __repr__(self) -> str: ...
    @overload
    def get(self, key: str, default: DefaultT) -> DefaultT | str | None: ...
    @overload
    def get(self, key: str, default: None = ...) -> str | None: ...
    @overload
    def sget(self, key: str, default: str | DefaultT) -> str | DefaultT: ...
    @overload
    def sget(self, key: str, default: str = "") -> str: ...

class LexborSelector:
    def __init__(self, node: LexborNode, query: str): ...
    def css(self, query: str) -> NoReturn: ...
    @property
    def matches(self) -> list[LexborNode]: ...
    @property
    def any_matches(self) -> bool: ...
    def text_contains(
        self, text: str, deep: bool = True, separator: str = "", strip: bool = False
    ) -> LexborSelector: ...
    def any_text_contains(
        self, text: str, deep: bool = True, separator: str = "", strip: bool = False
    ) -> bool: ...
    def attribute_longer_than(
        self, attribute: str, length: int, start: str | None = None
    ) -> LexborSelector: ...
    def any_attribute_longer_than(
        self, attribute: str, length: int, start: str | None = None
    ) -> bool: ...

class LexborCSSSelector:
    def __init__(self): ...
    def find(self, query: str, node: LexborNode) -> list[LexborNode]: ...
    def any_matches(self, query: str, node: LexborNode) -> bool: ...

class LexborNode:
    parser: LexborHTMLParser
    @property
    def mem_id(self) -> int: ...
    @property
    def child(self) -> LexborNode | None: ...
    @property
    def first_child(self) -> LexborNode | None: ...
    @property
    def parent(self) -> LexborNode | None: ...
    @property
    def next(self) -> LexborNode | None: ...
    @property
    def prev(self) -> LexborNode | None: ...
    @property
    def last_child(self) -> LexborNode | None: ...
    @property
    def html(self) -> str | None: ...
    def __hash__(self) -> int: ...
    def text_lexbor(self) -> str: ...
    def text(
        self, deep: bool = True, separator: str = "", strip: bool = False
    ) -> str: ...
    def css(self, query: str) -> list[LexborNode]: ...
    @overload
    def css_first(
        self, query: str, default: Any = ..., strict: Literal[True] = ...
    ) -> LexborNode: ...
    @overload
    def css_first(
        self, query: str, default: DefaultT, strict: bool = False
    ) -> LexborNode | DefaultT: ...
    @overload
    def css_first(
        self, query: str, default: None = ..., strict: bool = False
    ) -> LexborNode | None: ...
    def any_css_matches(self, selectors: tuple[str]) -> bool: ...
    def css_matches(self, selector: str) -> bool: ...
    @property
    def tag_id(self) -> int: ...
    @property
    def tag(self) -> str | None: ...
    def decompose(self, recursive: bool = True) -> None: ...
    def strip_tags(self, tags: list[str], recursive: bool = False) -> None: ...
    @property
    def attributes(self) -> dict[str, str | None]: ...
    @property
    def attrs(self) -> LexborAttributes: ...
    @property
    def id(self) -> str | None: ...
    def iter(self, include_text: bool = False) -> Iterator[LexborNode]: ...
    def unwrap(self) -> None: ...
    def unwrap_tags(self, tags: list[str], delete_empty : bool = False) -> None: ...
    def traverse(self, include_text: bool = False) -> Iterator[LexborNode]: ...
    def replace_with(self, value: bytes | str | LexborNode) -> None: ...
    def insert_before(self, value: bytes | str | LexborNode) -> None: ...
    def insert_after(self, value: bytes | str | LexborNode) -> None: ...
    def insert_child(self, value: bytes | str | LexborNode) -> None: ...
    @property
    def raw_value(self) -> NoReturn: ...
    def scripts_contain(self, query: str) -> bool: ...
    def scripts_srcs_contain(self, queries: tuple[str]) -> bool: ...
    def remove(self, recursive: bool = True) -> None: ...
    def select(self, query: str | None = None) -> LexborSelector: ...
    @property
    def text_content(self) -> str | None: ...

class LexborHTMLParser:
    def __init__(self, html: str| bytes ): ...
    @property
    def selector(self) -> "LexborCSSSelector": ...
    @property
    def root(self) -> LexborNode | None: ...
    @property
    def body(self) -> LexborNode | None: ...
    @property
    def head(self) -> LexborNode | None: ...
    def tags(self, name: str) -> list[LexborNode]: ...
    def text(
        self, deep: bool = True, separator: str = "", strip: bool = False
    ) -> str: ...
    @property
    def html(self) -> str | None: ...
    def css(self, query: str) -> list[LexborNode]: ...
    @overload
    def css_first(
        self, query: str, default: Any = ..., strict: Literal[True] = ...
    ) -> LexborNode: ...
    @overload
    def css_first(
        self, query: str, default: DefaultT, strict: bool = False
    ) -> LexborNode | DefaultT: ...
    @overload
    def css_first(
        self, query: str, default: None = ..., strict: bool = False
    ) -> LexborNode | None: ...
    def strip_tags(self, tags: list[str], recursive: bool = False) -> None: ...
    def select(self, query: str | None = None) -> LexborSelector | None: ...
    def any_css_matches(self, selectors: tuple[str]) -> bool: ...
    def scripts_contain(self, query: str) -> bool: ...
    def scripts_srcs_contain(self, queries: tuple[str]) -> bool: ...
    def css_matches(self, selector: str) -> bool: ...
    def clone(self) -> LexborHTMLParser: ...
    def unwrap_tags(self, tags: list[str], delete_empty : bool = False) -> None: ...

def create_tag(tag: str) -> LexborNode:
    """
    Given an HTML tag name, e.g. `"div"`, create a single empty node for that tag,
    e.g. `"<div></div>"`.
    """
    ...

def parse_fragment(html: str) -> list[LexborNode]:
    """
    Given HTML, parse it into a list of Nodes, such that the nodes
    correspond to the given HTML.

    For contrast, HTMLParser adds `<html>`, `<head>`, and `<body>` tags
    if they are missing. This function does not add these tags.
    """
    ...


class SelectolaxError(Exception):
    """An exception that indicates error."""
    pass
