import { useEffect, useState } from "react";
import "./../styles/timespent.css";

export default function TimeSpent({data}) {

    const minutesItem = data.find(el => el.type === "minutes");
    const otherItems = data.filter(el => el.type !== "minutes");


    return (
        <>
            <h1>
            You spent {minutesItem?.value} minutes with music this month
            </h1>

            <div className="list">
            {otherItems.map((el, i) => (
                <div key={i} className="song">
                <strong>{el.type}</strong>
                <p>{el.value}</p>
                </div>
            ))}
            </div>
        </>
    );

}