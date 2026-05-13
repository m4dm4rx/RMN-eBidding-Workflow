exports.handler = async (event) => {
  const target = (event.queryStringParameters ?? {}).url ?? '';

  if (!target.startsWith('https://opend.data.go.th/')) {
    return { statusCode: 403, body: 'Forbidden' };
  }

  try {
    const res = await fetch(target, {
      headers: { 'User-Agent': 'Mozilla/5.0' },
    });
    const body = await res.text();
    return {
      statusCode: res.status,
      headers: {
        'Content-Type': 'application/json; charset=utf-8',
        'Access-Control-Allow-Origin': '*',
      },
      body,
    };
  } catch (err) {
    return { statusCode: 502, body: String(err) };
  }
};
