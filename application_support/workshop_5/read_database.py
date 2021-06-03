import argparse
import contextlib
import getpass
import psycopg2


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'db_host',
        help='The DB host'
    )
    return parser.parse_args()


def connect(db_host, password):
    return psycopg2.connect(
        dbname='hacienda',
        host=db_host,
        port=5432,
        password=password,
        user='hacienda'
    )


def get_consignment_ids_for_warehouse(cursor, warehouse_code):
    sql = """
        SELECT oc.id
        FROM order_consignments oc
        INNER JOIN order_instructions oi ON oc.id = oi.consignment_id
        WHERE oc.warehouse_code = %s AND oi.state = 'Cancelled';
    """

    cursor.execute(sql, (warehouse_code, ))
    return cursor.fetchall()


def mark_instructions_as_cancelled(cursor, consignment_ids):
    sql = """
    UPDATE order_instructions SET state = 'Cancelled' WHERE consignment_id IN %s
    """
    # cursor.execute(sql, (tuple(consignment_ids), ))


def main():
    args = parse_arguments()
    connection = connect(args.db_host, getpass.getpass())
    warehouses = ["londongateway", "ktn_wh45"]
    cursor = connection.cursor()
    with contextlib.closing(cursor) as cursor:
        for warehouse in warehouses:
            cons_ids = get_consignment_ids_for_warehouse(cursor, warehouse)
            if not cons_ids:
                print(f"No consignments to cancel for {warehouse}")
                continue
            print(cons_ids)

            print(f"Going to cancel {len(cons_ids)} consignments for {warehouse}")
            mark_instructions_as_cancelled(cursor, cons_ids)
            connection.commit()

    print("Finished!")


if __name__ == '__main__':
    main()
