import DataBaseTool.dbConnect as db


def table_exits(table_name):
    return db.table_exists(table_name)


def create_table(table_name, columns):
    if db.table_exists(table_name):
        return
    create_table_sql = f'''
    CREATE TABLE {table_name} (
        `index` INT AUTO_INCREMENT PRIMARY KEY,
        '''
    for column in columns:
        create_table_sql += f"{column} VARCHAR(255), "
    create_table_sql = create_table_sql.rstrip(", ") + ")"  # 移除最后一个逗号并闭合括号
    db.update(create_table_sql)


def get_all(table_name):
    return db.select(f"select * from {table_name}")


def delete(table_name, index):
    sql = f"delete from {table_name} where `index`={index}"
    return db.update(sql)


def add(table_name, line_dict: dict):
    columns = "(" + ",".join(list(line_dict.keys())) + ")"
    vals = list(line_dict.values())
    for i in range(len(vals)):
        vals[i] = "'" + str(vals[i]) + "'"
    values = "(" + ",".join(vals) + ")"
    sql = f"insert into {table_name} {columns} VALUES {values}"
    return db.update(sql)


def get_max_id(table_name):
    sql = f"SELECT MAX(`index`) AS max_id FROM {table_name}"
    return db.select(sql)
