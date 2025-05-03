import multiprocessing

def sender(conn):
    conn.send("Hello from sender process!")
    conn.close()

def receiver(conn):
    msg = conn.recv()
    return msg

def ipc_demo_run():
    parent_conn, child_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=sender, args=(child_conn,))
    p.start()

    message = receiver(parent_conn)

    p.join()
    return {
        "Received Message": message
    }
