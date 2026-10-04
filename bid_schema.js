(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  root.BidSchema = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  const DEFAULTS = Object.freeze({
    deliveryDate: null,
    warrantyDueDate: null,
    retentionReturnStatus: 'unknown',
  });
  const RETURN_STATUSES = new Set(['unknown', 'not_returned', 'partially_returned', 'returned']);

  function normalizeDate(value) {
    return value === '' || value == null ? null : value;
  }

  function normalize(record = {}) {
    const normalized = { ...DEFAULTS, ...record };
    normalized.deliveryDate = normalizeDate(normalized.deliveryDate);
    normalized.warrantyDueDate = normalizeDate(normalized.warrantyDueDate);
    if (!RETURN_STATUSES.has(normalized.retentionReturnStatus)) {
      normalized.retentionReturnStatus = 'unknown';
    }
    return normalized;
  }

  function merge(existing, updates) {
    return normalize({ ...(existing || {}), ...updates });
  }

  return Object.freeze({ DEFAULTS, RETURN_STATUSES, normalize, merge });
});
