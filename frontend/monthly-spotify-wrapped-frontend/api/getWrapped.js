export async function getWrapped(userId) {
  const res = await fetch(
    `http://127.0.0.1:8000/wrapped/${userId}`
  );

  if (!res.ok) {
    throw new Error("Failed to fetch wrapped data");
  }

  return await res.json();
}