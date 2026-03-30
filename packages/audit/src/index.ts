/**
 * @vierp/audit v1.0.0
 * Comprehensive audit trail system for VietERP
 *
 * Re-exports all audit trail functionality
 */

// Types
export type {
  AuditEntry,
  AuditQueryOptions,
  AuditContext,
  Change,
} from "./types";
export { AuditAction } from "./types";

// Differ utilities
export { computeDiff, maskSensitiveData } from "./differ";

// Middleware
export { AuditMiddleware, withAudit } from "./middleware";

// Store implementations
export type { AuditStore } from "./store";
export { PrismaAuditStore, FileAuditStore } from "./store";

// Query helpers
export {
  queryAuditLog,
  getEntityHistory,
  getUserActivity,
  getModuleActivity,
  getActivityTimeline,
  countByAction,
  countByModule,
  getMostActiveUsers,
  getApprovalRequests,
  exportAuditLog,
  purgeOldEntries,
} from "./query";
