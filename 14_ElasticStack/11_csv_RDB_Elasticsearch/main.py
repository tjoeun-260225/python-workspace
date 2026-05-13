from db import create_table, insert_csv_to_mysql, fetch_all_books
from es_index import create_index, index_books
from search import search_by_title, search_by_publisher, search_top_loans, search_combined


def main():
    create_table()
    insert_csv_to_mysql()

    create_index()

    books = fetch_all_books()
    index_books(books)

    print("\n제목 검색: 흔한남매")
    for h in search_by_title("흔한남매"):
        print(f"  - {h['_source']['title']} (대출 {h['_source']['loan_count']}회)")

    print("\n출판사 검색: 아이세움")
    for h in search_by_publisher("아이세움"):
        print(f"  - {h['_source']['title']}")

    print("\n대출 TOP 5")
    for h in search_top_loans(5):
        print(f"  - {h['_source']['rank']}위 {h['_source']['title']} ({h['_source']['loan_count']}회)")

    print("\n복합 검색: 제목=과학 + 대출 30회 이상")
    for h in search_combined("과학", 30):
        print(f"  - {h['_source']['title']} (대출 {h['_source']['loan_count']}회)")


if __name__ == "__main__":
    main()
