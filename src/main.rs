use std::{thread, time::Duration};

use reqwest::Result;

fn main() -> Result<()> {
    for _i in 1..400 {
        thread::spawn(|| loop {
            reqwest::blocking::get("http://111.230.96.17");
        });
    }
    thread::sleep(Duration::from_secs(10000000));
    Ok(())
}
